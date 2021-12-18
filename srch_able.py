#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[5]:


from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)





def searchable(pdfpath):
    try:
        from PIL import Image
    except ImportError:
        import Image
    import pytesseract

    import numpy as np
    import pdf2image
    import os
    from pdf2image import convert_from_path as CFP
    from PyPDF2 import PdfFileReader, PdfFileWriter
    
    #filepaths relative to the current working directory
    pdfpath_cmd=pdfpath.replace(' ','_')
    FLDR=pdfpath_cmd[:-4]
    os.system('mkdir '+FLDR)
    print('image directory created: '+FLDR)
    
    IMGS=CFP(pdfpath,grayscale=True, dpi=300)
    print('pdf converted to imgs')
    
    
    JPEGPATHS=[]
    for k in range(len(IMGS)):
        IMGS[k].save(FLDR+'/'+str(k)+'.jpg')
        JPEGPATHS.append(FLDR+'/'+str(k)+'.jpg')
        
    print('imgs converted to jpegs and saved to '+FLDR)
    
    PDF_PAGES=[]
    for jpg in JPEGPATHS:
        print('processing: '+jpg)
        os.system('tesseract '+jpg+' '+jpg[:-4]+' PDF')
        print(jpg[:-4]+'.pdf'+' created')
        PDF_PAGES.append(jpg[:-4]+'.pdf')
    
    print('jpegs converted to searchable pdf pages and saved')
    
    print('merging')
    
    merge_pdfs(PDF_PAGES,pdfpath[:-4]+'_OCR'+'.pdf')
    
    os.system('rm -r '+FLDR)
    
    
    
        
        


# In[4]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




