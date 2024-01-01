import AutoBrowser

if __name__ == "__main__":
	OurBrowser = AutoBrowser.Browser()
	OurBrowser.direct_visit("https://orteil.dashnet.org/experiments/cookie/")
	OurBrowser.fast_click("/html/body/div[3]/div[6]/div[9]")
	

	OurBrowser.delay(180)