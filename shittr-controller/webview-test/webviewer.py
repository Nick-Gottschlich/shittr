import webview

window = webview.create_window('Hello world', 'http://localhost:3000', fullscreen=True)
webview.start()
# webview.start(print(window.get_current_url()))

# print ('whodat')
# fakeButtonPress = input()
# if fakeButtonPress == 'go':
#     print(window.get_current_url())