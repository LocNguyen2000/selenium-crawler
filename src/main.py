from selenium import webdriver

driver_path = '/home/loc/Documents/Web Driver/91/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://shopee.vn/')
# selector_shop = "#main > div > div._193wCc > div > div.shop-page > div > div.shop-page-menu > div > div > div > " \
#                 "a.navbar-with-more-menu__item.navbar-with-more-menu__item--active "
# selector_product = "#main > div > div._193wCc > div.page-product > div.container > div._2G_fvP > " \
#                    "div._34c6X6.page-product__shop > div._3-NiSV > div > div._3uf2ae "

driver.close()

