import getpass
import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
driver = None

'''
command line option arguments for multiple browser
'''


def pytest_addoption(parser):
    parser.addoption("--browser_choice", action="store", default="chrome",
                     help="choose any browser from options : chrome, firefox, ie")


@pytest.fixture(scope="class")
def setup(request):
    global driver

    # getting os platform
    os_platform = sys.platform
    print(f"Executing Tests on {os_platform}")

    # get logged in system username
    username = getpass.getuser()

    # retrieve command line argument
    browser_name = request.config.getoption("--browser_choice")
    print(browser_name)
    if browser_name.lower() == "chrome":
        if os_platform == "linux":
            print("inside linux")
            path = "usr/bin/chromedriver"
            print(path)
            options = Options()
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_experimental_option("useAutomationExtension", False)
            driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            #serv = "C:\\Users\\" + username + "\\Downloads\\chromedriver_win32_v87\\chromedriver.exe"
            #driver = webdriver.Chrome(executable_path=serv)
    elif browser_name.lower() == "firefox":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge(executable_path="C:\\Users\\" + username + "\\Downloads\\edgedriver_win64_v87.0664\\msedgedriver.exe")
    elif browser_name.lower() == "ie":
        driver = webdriver.Ie(executable_path="C:\\Users\\" + username + "\\Downloads\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")

    driver.maximize_window()
    driver.get("http://amazon.com")
    request.cls.driver = driver
    yield
    driver.close()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)

