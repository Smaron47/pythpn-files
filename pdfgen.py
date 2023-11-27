import pdf2image
import PIL
import pytesseract

pytesseract.pytesseract.tesseract_cmd="tesseract"
f=open("pdfgen.pdf","w+b")
K=input("Enter the Pdf Path => ")
k=K.replace("'","")
def pdf(es):
        #m=filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    d=pdf2image.convert_from_path(es)
    for s in d:
        s2="sdf"+".jpg"
        s.save(s2, "JPEG")

        wp=PIL.Image.open(s2)
        sf=pytesseract.image_to_pdf_or_hocr(wp,lang="ben")
        print(sf)
        f.write(sf)
print(k)
pdf(k)
f.close()
        