#imports
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


base_url_lms = "http://lms.uaf.edu.pk/login/index.php"
base_url_attendance_portal="http://121.52.152.24/"
driver=webdriver.Chrome(executable_path='F:\Outputs\Python Outputs\Web Scraping\Overall Result Compare\chromedriver.exe')
over_all_result = list()


def lms_gpa_adder(ag):
    #load the web browser
    driver.get(base_url_lms)
    #get the elements
    ag_no_field = driver.find_element_by_id("REG")
    search_btn = driver.find_element_by_xpath("/html/body/div[3]/div/section/div/div/div/div[4]/div[1]/div[2]/div/div[1]/form/div[2]/input[3]")
    #enter the ag no into the feild and serach
    ag_no_field.send_keys(ag)
    ActionChains(driver).click(search_btn).perform()
    rows = len(driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr"))
    cols = len(driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr[2]/td"))

    for i in range(2,rows+1):
        course_code = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(i)+"]/td[4]")).text.upper()
        total_marks = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(i)+"]/td[11]")).text.upper()
        sub_result = list()
        sub_result.append(course_code)
        sub_result.append(total_marks)
        over_all_result.append(sub_result)

def attendance_portal_result(ag):

    driver.get(base_url_attendance_portal)

    search_field = driver.find_element_by_id("ctl00_Main_txtReg")
    search_btn = driver.find_element_by_id("ctl00_Main_btnShow")

    search_field.send_keys(ag)
    ActionChains(driver).click(search_btn).perform()

    result_information_btn = driver.find_element_by_xpath("/html/body/form/div[5]/div/div[1]/span[3]/span/span/span")
    ActionChains(driver).click(result_information_btn).perform()

    rows = len(driver.find_elements_by_xpath("/html/body/form/div[5]/div/div[2]/div[3]/div/table/tbody/tr"))

    for i in range(2,rows+1):
        course_code = (driver.find_element_by_xpath("/html/body/form/div[5]/div/div[2]/div[3]/div/table/tbody/tr["+str(i)+"]/td[6]")).text.upper()
        total_marks = (driver.find_element_by_xpath("/html/body/form/div[5]/div/div[2]/div[3]/div/table/tbody/tr["+str(i)+"]/td[13]")).text.upper()
        decimal_index = total_marks.index(".")
        total_marks = total_marks[0:decimal_index]
        sub_result = list()
        sub_result.append(course_code)
        sub_result.append(total_marks)
        over_all_result.append(sub_result)

    driver.close()

def extra_data_remover(all_result):
    result_list = all_result
    unique_list = list()
    for i in result_list:
        if i not in unique_list:
            unique_list.append(i)            

    return unique_list


lms_gpa_adder("2019-ag-6081")
attendance_portal_result("2019-ag-6081")
print(over_all_result)
print(len(over_all_result))
print("============================================================================")

removerd_list = extra_data_remover(over_all_result)
print(removerd_list)
print(len(removerd_list))




