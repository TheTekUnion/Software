from bs4 import BeautifulSoup
import urllib.request

current_version = "1.0.0"


def get_info():

    html_file = urllib.request.urlopen("http://thetekunion.com/software/console_applications/console_universal_calculator/index.php")

    html = html_file.read()

    soup = BeautifulSoup(html, "html.parser")

    version_names = []
    version_files = []

    for info in soup.find_all("span", {"class": "console_uni_calc"}):
        version_names.append(info["id"])

    for link in soup.find_all("a", {"class": "console_uni_calc"}):
        version_files.append(link["href"])

    latest_version = version_names[0]

    version_info_dict = dict(zip(version_names, version_files))

    return [version_info_dict, latest_version]


def get_download_link(version_dict, version_num):
    return version_dict[version_num]


def needs_update(cur_ver, latest_ver):
    if latest_ver > cur_ver:
        return True
    else:
        return False


def update(cur_ver, latest_ver, web_page, download_link):
    print("An update is available for the Console Universal Calculator. ")
    print("Current version: " + cur_ver)
    print("Latest version: " + latest_ver)
    print("Visit the Console Universal Calculator web page: " + web_page)
    print("Download the latest version: " + download_link)


def update_check():
    version_info_dictionary = get_info()[0]
    latest_version_name = get_info()[1]

    if needs_update(current_version, latest_version_name):
        wep_page = "http://thetekunion.com/software/console_applications/console_universal_calculator/index.php"

        download_file_name = get_download_link(version_info_dictionary, latest_version_name)

        download_link = "http://thetekunion.com/software/console_applications/console_universal_calculator/" + download_file_name

        update(current_version, latest_version_name, wep_page, download_link)
    else:
        print("You have the latest version of the Console Universal Calculator. ")





