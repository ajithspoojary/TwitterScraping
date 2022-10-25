import requests
class lottie_anim:
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
   # lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_nkf5e15x.json")
    lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_nkf5e15x.json")
    lottie_coding1 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_hmdwlaed.json")