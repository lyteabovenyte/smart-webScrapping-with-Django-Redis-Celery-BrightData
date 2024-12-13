from bs4 import BeautifulSoup

def extract_title_and_price(html):
    soup = BeautifulSoup(html, "html.parser")
    productTitle = soup.find('span', id='productTitle')
    productTitleText = f'{productTitle.text}'.strip()
    productPrice = soup.find_all('span', class_='a-price-whole')[0]
    productPriceText = "".join([x for x in f"{productPrice.text}".strip() if x.isdigit() or x == "."])
    productPriceNum = float(productPriceText)
    return (productTitleText, productPriceNum)
