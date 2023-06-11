from SeleniumBrowser import SeleniumBrowser
import threading

progression = 0
total_count = 1


def progression_log():
    global progression
    global total_count
    progression += 1
    print(f"Progression: {round(progression / total_count * 100, 2)}%")


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

    progression_log()
    browser.close()


def read_url(file_path="urls.txt"):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        urls = file_contents.split('\n')
        return urls


def main():
    urls = read_url()
    global total_count
    total_count = len(urls)

    threads = []
    for url in urls:
        thread = threading.Thread(target=download_video(url))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Download complete")


if __name__ == '__main__':
    main()
