        from selenium import webdriver
        import time
        import pyautogui

        navegador = webdriver.Edge()
        navegador.maximize_window()
        navegador.get("https://prod-srs-collect-la.io.gmfinancial.com/Collections/servlet/common.CollectionsCommonGatewayServlet?requestID=5")

        #login
        navegador.find_element_by_xpath('//*[@id="User_ID"]').send_keys('LX3PHT')
        navegador.find_element_by_xpath('//*[@id="TxtPWD"]').send_keys('Gmac*789')
        time.sleep(2)
        navegador.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td[2]/a/img').click()

        #Core Colecttion
        navegador.find_element_by_xpath('//*[@id="mainbody"]/form/table[1]/tbody/tr[6]/td/button').click()
        navegador.find_element_by_xpath('/html/body/div[1]/div[3]').click()
        navegador.find_element_by_xpath('/html/body/div[4]/div[3]').click()

        #Abrir outra aba para o 233
        pyautogui.hotkey('ctrl','t')
        time.sleep(2)
        pyautogui.click(x=109, y=43)
        pyautogui.write('10.10.0.233/robos/srs_cob/')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(10)

        #Repetição
        rep = 1
        for rep in range(1,500):

        #acesso link 233
        pyautogui.doubleClick(x=23, y=280)
        time.sleep(1)
        pyautogui.hotkey('ctrl','c')
        time.sleep(1)

        #Voltar SRS
        pyautogui.click(x=170, y=17)
        navegador.find_element_by_xpath('//*[@id="txtCardNumber"]').click()
        time.sleep(1)
        navegador.find_element_by_xpath('//*[@id="txtCardNumber"]').click()
        time.sleep(1)
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        navegador.find_element_by_xpath('/html/body/form[1]/fieldset/table[2]/tbody/tr/td[2]/button[2]').click()

        #Repetição quando não tiver contrato
        #contrato = (navegador.find_element_by_xpath('/html/body/form[1]/table[3]/tbody/tr[3]/td'))
        #if contrato == "No Data Found":
        #pyautogui.click(x=384, y=14)
        #time.sleep(1)
        #pyautogui.click(x=140, y=323)
        #time.sleep(12)
        #continue
        #Final da Repetição

        navegador.find_element_by_xpath('/html/body/form[1]/table[3]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/a').click()
        time.sleep(5)

        #Show Follow Up
        pyautogui.click(x=989, y=125)
        time.sleep(1)
        pyautogui.click(x=570, y=620)
        time.sleep(1)
        pyautogui.write('025')
        time.sleep(1)
        pyautogui.hotkey('enter')

        #copiar ocorrencianão atende.. não atende..ANA PAULABoa tarde sr. StellaAPANA PAULASou a Ana Paula do Escritório
        Eduardo Albuquerque Assessoria jurídica da Chevrolet.tudo bem?APANA PAULAGostaria de falar com a Sr. referente o
        veiculoAPANA PAULAestamos com uma proposta de quitação para o seu contratopodemos conversar?
        pyautogui.hotkey('alt','tab')
        pyautogui.click(x=416, y=18)
        time.sleep(1)
        pyautogui.click(x=202, y=279)
        time.sleep(1)
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')

        #colocar a ocorrencia no SRS
        pyautogui.hotkey('alt','tab')
        pyautogui.click(x=230, y=688)
        time.sleep(2)
        pyautogui.hotkey('ctrl','v')
        pyautogui.click(x=1083, y=660)
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.click(x=1213, y=125)
        time.sleep(2)

        #positivar
        pyautogui.click(x=51, y=321)
        time.sleep(12)