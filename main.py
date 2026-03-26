from SeleniumBrowser import SeleniumBrowser

progression = 0
total_count = 1
url_file_path = "urls.txt"
debug = True
headless = True

log = lambda x : print(x) if debug else None

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

def error_recovery(url):
    global url_file_path
    print("The previouse download failed, we leave it in the list")
    with open(url_file_path, 'a') as file:
        file.write('\n' + url)


def download_video(music_url):
    global headless
    converter_url = "https://ytmp3.cc/Nnht/"
    browser = SeleniumBrowser(converter_url, headless=headless)
    error = False
    try:
        log("********************************************")
        log("Browser init finish, going to website ...")
        input_url_field = browser.get_element_by_id("v")
        browser.fill_input(input_url_field, music_url)

        xpath = "/html/body/div[2]/form/div[3]/div[2]/button"
        start_convert_btn = browser.get_element_by_xpath(xpath, timeout=30)
        browser.click_button(start_convert_btn)
        log("Waiting for convertion ...")

        xpath = "/html/body/div[2]/form/div[3]/button[1]"
        start_download_btn = browser.get_element_by_xpath(xpath, timeout=60)
        browser.click_button(start_download_btn)
        log("Waiting to download ...")
    except Exception as e:
        error = True
        print(e)
        error_recovery(music_url)  
    finally:
        browser.close()
        post_download()
        log("********************************************\n")
    return error


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
        


    print("Download complete")


if __name__ == '__main__':
    main()
