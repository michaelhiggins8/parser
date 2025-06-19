from fastapi import APIRouter
from fastapi.responses import FileResponse      
import zipfile

router = APIRouter()

@router.get("/parse")
def parse_file():

    #get content as decimal bytes
    with open("routes/sample.env", "rb") as f:
        data = list(f.read())

    headerStartPattern = [37,37] #%%
    headerEndPattern = [95, 83, 73, 71, 47, 68, 46, 67, 46] #_SIG/D.C.
    webpPattern = [82, 73, 70, 70] #RIFF
    xmlPattern = [60, 63, 120, 109 ] #<?xm
    inHeader = False
    fileNames = []    


    # iterate through each byte (as decimal)
    for i in range(0,len(data)):

        #mark that we are in header section  
        if( i<= len(data) - 2 and data[i:i+2] == headerStartPattern):
            inHeader = True
        #mark that we are in body 
        if( i >=9 and inHeader  and  data[i-9:i] == headerEndPattern):
            #get start of body and end of body
            startOfSection = i+4
            endOfSection = startOfSection + data[i] + 256*data[i+1] + 65536*data[i+2] + 16777216*data[i+3]
            
            #write the body as webP file if the file starts as webP
            if(data[startOfSection:startOfSection+4] ==webpPattern):
                with open(f"output{i}.webp", "wb") as f:
                    f.write(bytes(data[startOfSection:endOfSection]))
                fileNames.append(f"output{i}.webp")
                #return FileResponse(f"output{i}.webp") 
                
            #write the body as xml file if the file starts as xml
            elif(data[startOfSection:startOfSection+4] ==xmlPattern):
                with open(f"output{i}.xml", "wb") as f:
                    f.write(bytes(data[startOfSection:endOfSection]))
                fileNames.append(f"output{i}.xml")

            
            #write the body as txt file if the file starts if type unknown
            else:
                with open(f"output{i}.txt", "wb") as f:
                    f.write(bytes(data[startOfSection:endOfSection]))
                fileNames.append(f"output{i}.txt")
            #mark that we left header section (are now in body)
            inHeader = False


    #zip contents
    with zipfile.ZipFile("all_outputs.zip", "w") as zf:   
        for p in fileNames:                      
            zf.write(p) 
    #return zip as response
    return FileResponse("all_outputs.zip") 

    
    
    




