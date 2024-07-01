import pdfkit





def url_to_pdf(url):
    pdfkit.from_url(url, "out.pdf")
    