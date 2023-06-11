from SeleniumBrowser import SeleniumBrowser

progression = 0
total_count = 1
url_file_path = "urls.txt"


def post_download():
    global progression
    global total_count
    global url_file_path

    progression += 1
    print(f"Progression: {round(progression / total_count * 100, 2)}%")

    # Remove downloaded url
    with open(url_file_path, 'r') as file:
        lines = file.readlines()

    with open(url_file_path, 'w') as file:
        file.writelines(lines[1:])


def download_video(music_url):
    converter_url = "https://ytmp3.nu"
    browser = SeleniumBrowser(converter_url, headless=True)

    input_url_field = browser.get_element_by_id("url")
    browser.fill_input(input_url_field, music_url)

    xpath = "/html/body/form/div[2]/input[3]"
    start_convert_btn = browser.get_element_by_xpath(xpath)
    browser.click_button(start_convert_btn)

    xpath = "/html/body/form/div[2]/a[1]"
    start_download_btn = browser.get_element_by_xpath(xpath)
    browser.click_button(start_download_btn)

    browser.close()


def read_url(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        urls = file_contents.split('\n')
        return urls


def main():
    global url_file_path
    urls = read_url(url_file_path)
    global total_count
    total_count = len(urls)

    for url in urls:
        download_video(url)
        post_download()

    print("Download complete")


if __name__ == '__main__':
    main()
