import contextlib
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common import action_chains, keys


date_field_id = "ReportViewer1_ctl08_ctl03_txtValue"
print_field_id = "ReportViewer1_ctl09_ctl06_ctl00_ctl00_ctl00"
dialog_print_button_class = 'msrs-printdialog-pprintbutton'
dialog_download_button_class = 'msrs-printdialog-downloadlink'

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": r"/files",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True
})


#with contextlib.closing(webdriver.Chrome) as browser:
browser = webdriver.Chrome(options=options)
browser.get("http://aplicaciones.pima.go.cr/Reportes/Boletin_Precios_Fecha.aspx")

# Wait for "Ver Informe Link" to be visible
wait = ui.WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.ID, date_field_id)))

date_field = browser.find_element_by_id(date_field_id)
date_field.clear()
date_field.send_keys("26/04/2019")

browser.find_element_by_id('ReportViewer1_ctl08_ctl00').click()

time.sleep(2)
wait.until(EC.invisibility_of_element((By.NAME, 'CancelLinkText')))

print_button = browser.find_element_by_id(print_field_id)
print_button.click()

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, dialog_print_button_class)))
dialog_print_button = browser.find_element_by_class_name(dialog_print_button_class)
dialog_print_button.click()

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, dialog_download_button_class)))
dialog_download_button = browser.find_element_by_class_name(dialog_download_button_class)
dialog_download_button.click()




#wait = ui.WebDriverWait(browser, 10)
#wait.until(EC.presence_of_element_located((By.XPATH, "//div[@style='width:36.05mm;min-width: 36.05mm;']")))

#wait.until(EC.element_to_be_clickable((By.ID, "ReportViewer1_ctl09_ctl04_ctl00_ButtonImgDown")))
#browser.find_element_by_id('ReportViewer1_ctl09_ctl04_ctl00_ButtonImgDown').click()

#browser.execute_script("$find('ReportViewer1').exportReport('PDF');");

menu = browser.find_element_by_id('ReportViewer1_ctl09_ctl04_ctl00_Menu')
element = browser.find_element_by_xpath('//*[@title="PDF"]')

x = 0

#element = menu.find_element_by_link_text('PDF')
#if element is not None:
#    element.send_keys(keys.Keys.ENTER)



#menu.click()
#element = browser.find_element_by_xpath("//div[contains(@id,'ReportViewer1_ctl09_ctl04_ctl00_Menu')]/a")
#element.click()

    #browser.execute_script("$find('ReportViewer1').exportReport('PDF');");

    #element = browser.find_element_by_class_name('ActiveLink')

    #print(element.get_text())


