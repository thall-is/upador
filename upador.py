def upador():
    from webdriver_manager.chrome import ChromeDriverManager
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    import os
    import sys





    def menu():

        print("|***************************************|\n")
        print(" gostaria de subir quais produtos hoje ?\n")
        print(' [0] - acessorios\n'
              ' [1] - aneis\n'
              ' [2] - berloques\n'
              ' [3] - brincos\n'
              ' [4] - chokers\n'
              ' [5] - pingentes\n'
              ' [6] - pulseiras\n'
              ' [7] - relicarios\n'
              ' [8] - tornozeleiras\n'
              ' [9] - charms\n'
              ' [10] - sair\n'
              ' [all] - continuar buscando\n')
        print("|***************************************|\n")
        t = input('????? : ')
        print(f'selecionado {t}')
        return t

    def endereco(t):
        sub_pasta = ' '
        print(sub_pasta)
        print('procurando endereco')
        print(t)
        type(t)
        if t == '0' or t == 0:
            print('pasta de acessorios !')
            sub_pasta = r'\Root\acessorios\temp'
        elif t == '1'or t == 1:
            print('pasta de aneis selecionada !')
            sub_pasta = r'\Root\aneis\temp'
        elif t == '2'or t == 2:
            print('pasta de berloques selecionada !')
            sub_pasta = r'\Root\berloques tratados\temp'
        elif t == '3'or t == 3:
            print('pasta de brincos selecionada !')
            sub_pasta = r'\Root\brincos\temp'
        elif t == '4'or t == 4:
            print('pasta de chokers selecionada !')
            sub_pasta = r'\Root\chokers\temp'
        elif t == '5'or t == 5:
            print('pasta de pingentes selecionada !')
            sub_pasta = r'\Root\pingentes\temp'
        elif t == '6'or t == 6:
            print('pasta de pulseiras selecionada !')
            sub_pasta = r'\Root\pulseiras\temp'
        elif t == '7'or t == 7:
            print('pasta de relicarios selecionada !')
            sub_pasta = r'\Root\relicarios\temp'
        elif t == '8' or t == 8:
            print('pasta de tornozeleiras selecionada !')
            sub_pasta = r'\Root\tornozeleiras\temp'
        elif t == '9'or t == 9:
            print('pasta de charms selecionada !')
            sub_pasta = r'\Root\charms\temp'
        elif t == '10'or t == 10:
            print(f'{t}')
            print('sair')
            sys.exit('finalizado')

        pasta = r"C:\Users\thallys\Pictures" + sub_pasta
        print(pasta)

        return pasta

    def verif_ark():

        list_sku = []
        list_caminho = []

        if selecao == 'all':
            alcance_max = 10
            alcance_min = 0
        else:
            alcance_max = int(selecao)+1
            alcance_min = int(selecao)


        for k in range(alcance_min,alcance_max):
            print(f'valor de k :{k}')
            ev_pasta = endereco(k)
            print(f'diretorio-{ev_pasta}')
            for address, dirs, files in os.walk(ev_pasta):
                for name in files:

                     nome = os.path.join(name)[-10:-4]
                     print(f'{nome}')
                     endereco_ark = os.path.join(address, name)
                     print(f'{endereco_ark}')
                     #sku = nome[-10:-4]

                     if nome[0] == '6' or nome[0] == '5' or nome[0] == '3' or nome[0] == '2' or nome[0] == '1' and len(nome) == 5 or len(nome) == 4:
                        #list_nome = [sku]
                        list_sku.append(nome)
                        #list_endereço = [endereço]
                        list_caminho.append(endereco_ark)



        if len(list_sku) == 0 :
            print('Não existem skus disponiveis no momento')

            if selecao == 'all':
                print('iniciando espera')
                espera(60,1)
                print('buscando novamente')
                return 0
            else:
                return 1



        else:
            print('Imagens encontradas\n')
            for i in range(0, len(list_sku)):

                print(f'[{list_sku[i]}]'+' - '+f'[{list_caminho[i]}]')

            return list_sku,list_caminho

    def loggin():

            arquivo = open('info_loggin.txt', 'r')
            email_loggin = arquivo.readline()
            senha_loggin = arquivo.readline()
            arquivo.close()

            try:
                email_path = ('#email')
                password_path = '#render-admin\.login-legacy\.home > div > div > div > div.ph7-ns.ph4.mb3 > div.mw6.mt7.center > div:nth-child(1) > div > div.mb5 > label > div > input'

                print('acessando o site...')

                site_login = 'https://bijutotal.myvtex.com/admin'

                driver.get(site_login)
                #driver.minimize_window()

                print('Iniciando login')
                test = 0
                email_box = driver.find_element(By.CSS_SELECTOR, email_path)
                email_box.click()
                print('Inserindo email...')
                print(f'{email_loggin}')
                email_box.send_keys(email_loggin + Keys.ENTER)

                password_box = driver.find_element(By.CSS_SELECTOR, password_path)
                password_box.click()
                test = driver.find_element(By.CSS_SELECTOR, password_path).is_displayed()
                print('Inserindo a senha...')
                password_box.send_keys(senha_loggin + Keys.ENTER)

                print('|Senha inserida!|')

                driver.implicitly_wait(0)
                sleep(3)
                sms = driver.find_element(By.XPATH,'//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[1]').is_displayed()

                while sms == 1:
                    print('Codigo sms requisitado !')
                    codigo_de_acesso = input('|Insira o codigo |\n:')
                    sms_patch = driver.find_element(By.XPATH, '//*[@id="requestsmscode_code"]')
                    sms_patch.click()
                    sms_patch.send_keys(codigo_de_acesso + Keys.ENTER)
                    cod_invalid = driver.find_element(By.XPATH,'//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[3]/label/div[2]').is_displayed()
                    sms = driver.find_element(By.XPATH,'//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[1]').is_displayed()

                    if cod_invalid == 1:
                        desc_cod_invalid = driver.find_element(By.XPATH, '//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[3]/label/div[2]')
                        print(desc_cod_invalid.text)
                        sms_patch = driver.find_element(By.XPATH, '//*[@id="requestsmscode_code"]')
                        webdriver.ActionChains(driver).double_click(sms_patch).perform()
                        sms_patch.send_keys(Keys.DELETE)

            except NoSuchElementException:
                pass

            return test

    def sub_pagina():
            espera(5, 1)
            ul_sub = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="skuTabNavigation"]/li[@class="active"]'))).text
            print(ul_sub)
            return ul_sub

    def espera(v,s):
            for i in range(0,v):
                sleep(s)
                print('.')

    def pagina_img():
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="skuTabNavigation"]/li[1]/a'))).click()
            print('sku ' + sku)
            print('verificando se existe imagens associadas')
            driver.find_element(By.XPATH, '//*[@id="skuTabNavigation"]/li[2]/a').click()

            try:
                driver.find_element(By.XPATH,'//*[@id="ctl00_Conteudo_tbxIdArquivoControle_rptArquivos_ctl0_txtTextoImagem"]')
                print('já existem imagens associadas a esste Sku')

            except NoSuchElementException:
                print('não existe imagens associadas')
                pass

            print('adicionando nova imagem')
            inserir_ark = driver.find_element(By.XPATH, '//*[@id="ctl00_Conteudo_tbxIdArquivoControle_lnkInserirArquivo"]')
            espera(3, 1)
            inserir_ark.click()
            espera(3, 1)
            print('inserir')
            driver.find_element(By.XPATH, '//*[@id="ctl00_Conteudo_tbxIdArquivoControle_tbxArquivo"]').send_keys(list_caminho[i])
            espera(3, 1)
            driver.find_element(By.XPATH, '//*[@id="ctl00_Conteudo_tbxIdArquivoControle_btnEnviar"]').click()
            print('enviar')

            espera(8, 2)

            aba_sku = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="skuTabNavigation"]/li[2]/a')))
            aba_sku.click()

            try :
                error_mesage_img = driver.find_element(By.NAME,'The file size is too large. Please send a file with a maximum of 3000 KB.')
                print(f'{error_mesage_img.text}')
                list_img_format_error.append(list_sku[i])
            except NoSuchElementException:
                pass
            try :
                error_mesage_img_2 = driver.find_element(By.XPATH,'//*[@id="ctl00_Conteudo_tbxIdArquivoControle_mcAlerts_rptMessages_ctl01_liMessage"]')
                print(f'{error_mesage_img_2.text}')
                list_img_format_error.append(list_sku[i])
            except NoSuchElementException:
                pass

            elements_fitext = driver.find_elements(By.XPATH,('//*[contains(@id,"txtTextoImagem")]'))
            print(str(len(elements_fitext)) + ' elementos imagem')
            print('estou procurando o : ' + sku)

            for j in range(0, len(elements_fitext)):

                path_value_sku ='//*[@id="ctl00_Conteudo_tbxIdArquivoControle_rptArquivos_ctl0' + str((j+1)) + '_txtTextoImagem"]'
                value_sku_drv = driver.find_element(By.XPATH,path_value_sku)
                value_sku = value_sku_drv.get_attribute('value')
                print(value_sku)
                if value_sku == sku:
                    try:
                        path_tornar_principal = '//*[@id="ctl00_Conteudo_tbxIdArquivoControle_rptArquivos_ctl0' + str((j+1)) + '_lnkTornarPrincipal"]'
                        driver.find_element(By.XPATH, path_tornar_principal).click()
                        print('imagem encontrada tornando a principal')
                        print('imagem ' + sku + ' principal')
                        break
                    except NoSuchElementException:
                        print('a imagem ' + sku + ' é a principal')
                        break
            trigger_img = 1
            return trigger_img

    def verif_stoque(sk):
        driver.get(f'https://bijutotal.myvtex.com/admin/inventory/?keyword={sk}&skuId={sk}')
        espera(5,1)
        wait.until(frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app-content"]/main/iframe')))
        espera(3,1)
        Disponivel = driver.find_element(By.XPATH,'//*[@id="render-admin.app.inventory"]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div[1]/table/thead/tr/th[7]/span').text
        print(f'{Disponivel}')
        if Disponivel == 'Disponível':
            estoque = driver.find_element(By.XPATH,'//*[@id="render-admin.app.inventory"]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div[1]/table/tbody/tr/td[7]/span/div/span').text
            print(f'{estoque}')

        if estoque != '0':
            return True
        else:
            return False

    def verif_preco(sk,cod):
        driver.get('https://bijutotal.myvtex.com/admin/pricing/#/prices/?tradePolicy=1&page=1&qtd=10')
        espera(5,1)
        wait.until(frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app-content"]/main/iframe')))
        espera(3,1)
        driver.find_element(By.XPATH, '//*[@id="s2id_role-input-search"]/ul/li').click()
        driver.find_element(By.XPATH,'//*[@id="s2id_autogen1"]').send_keys(f'{sk}')
        espera(3,1)
        driver.find_element(By.XPATH, '//*[@id="s2id_autogen1"]').send_keys(Keys.ENTER)
        espera(3, 1)
        for l in range(1,99):
            patch_test_loc = f'//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]/div[{l}]/div[1]/div/div[1]/div[2]'
            print(f'{patch_test_loc}')
            test_loc = driver.find_element(By.XPATH,patch_test_loc)
            if test_loc.text == cod:
                preco_patch = f'//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]/div[{l}]/div[1]/div/div[2]/div[2]/div[1]'
                preco_test = driver.find_element(By.XPATH,preco_patch)
                preco = preco_test.text
                espera(2,1)

                print(f'{preco}')

                if preco != '0,00' or preco != '':
                    return True
                else:
                    return False



                ##'//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]'
                ##'//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]/div[3]'
               ##f'//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]/div[{l}]/div[1]/div/div[1]/div[2]'
               ## '//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[1]'
               ##f'//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]/div[{l}]/div[1]/div/div[1]/div[2]'
            ##    '//*[@id="app-content"]/div[1]/div[3]/div[3]/div/div/product-container/div/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div[2]'
    rodando = True
    check = False

    while rodando == True:

        if check == True:
            selecao = 'all'
        else:
            selecao = menu()

        first_run = 0

        while first_run == 0 or first_run == 1:

            print(selecao)
            first_run = verif_ark()
            print(f'esse e o valor de {first_run}')

            if first_run == 0 or first_run == 1 :

                while first_run <= 1:

                    if first_run == 1:
                        selecao = menu()
                        print(selecao)
                        print(f'esse e o valor de {first_run} dentro do if')
                    break
            if first_run != 0 and first_run != 1 :
                list_sku, list_caminho = first_run
                break




        #list_sku,list_caminho = verif_ark()

        print(list_sku,list_caminho)

        # aqui começa o selenium operando o sku e subindo as img

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver = webdriver.Chrome(r"chromedriver.exe")
        driver.implicitly_wait(20)
        wait = WebDriverWait(driver, timeout=40, poll_frequency=0.5)



        if len(list_sku) != 0 and loggin() == 1:
            print('|Admin carregado !|')
            #espera(5,1)
            botao_esq_sup = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="topbar-vtex"]/div[1]/div/div/button')))
            botao_esq_sup.click()
            #driver.find_element(By.XPATH, '//*[@id="topbar-vtex"]/div[1]/div/div/button').click()

        list_manual = []
        list_sku_ok = []
        list_sku_color_error = []
        list_img_format_error = []
        list_sku_number_error = []
        list_sem_estoque = []
        list_sem_preco = []
        list_inativo = []

        Break_point = False

        for i in range(0,len(list_sku)):

            while True:

                sku = list_sku[i]

                print('acessando sku ' + sku)

                driver.get('https://bijutotal.myvtex.com/admin/Site/SkuForm.aspx?IdSku=' + sku)

                espera(6,1)

                wait.until(frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app-content"]/main/div/iframe')))
                print('dentro do iframe')

                try:
                    espera(5,1)
                    error_mesage = driver.find_element(By.XPATH,'//*[@id="error-container"]/div[1]/div[1]')
                    print(f'{error_mesage.text}')
                    list_sku_number_error.append(list_sku[i])
                    if i < (len(list_sku) - 1):
                        i =+ i
                    else:
                        Break_point = True
                        break

                except NoSuchElementException:
                    break
                    pass

            print(f'valor de break_point = {Break_point}')
            if Break_point == True:
                break


            espera(3,1)

            janela_img = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="skuTabNavigation"]/li[2]/a')))
            espera(1,1)
            webdriver.ActionChains(driver).double_click(janela_img).perform()

            img_pass = 0

            if sub_pagina() == 'Imagens':
                img_pass = pagina_img()
                tab_sku = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="skuTabNavigation"]/li[1]/a')))
                tab_sku.click()

            if sub_pagina() == 'SKU':
                if img_pass == 0:
                    img_pass = pagina_img()
                    print(f'o valor de img_pass é : {img_pass}')

                patch_cod_ref = driver.find_element(By.XPATH,'//*[@id="ctl00_Conteudo_tbxCodigoReferencia_txtId"]')
                cod_ref = patch_cod_ref.get_attribute('value')

                patch_nome_sku = driver.find_element(By.XPATH,'//*[@id="ctl00_Conteudo_tbxNome_txtId"]')
                cod_nome_sku = patch_nome_sku.get_attribute('value')
                print(f'{cod_nome_sku}')

                sku_ativo = driver.find_element(By.XPATH, '//*[@id="ctl00_Conteudo_chkFlagAtiva"]')

                sku_ativo_box = driver.find_element(By.XPATH, '//*[@id="ctl00_Conteudo_chkFlagAtivateIfPossible"]')

                driver.find_element(By.XPATH, '//*[@id="skuTabNavigation"]/li[4]/a').click()

                espera(3,1)

                try:
                    doble_check = 0
                    list_sku_names_text = []
                    list_sku_names_text_def = []

                    while doble_check < 2:

                        try:
                            error_report = driver.find_element(By.XPATH,'//*[@id="ctl00_Conteudo_ctrlEspecificacao_pnlEmptyProdutoCampoValor"]/span').text
                            print(f'{error_report}')
                            doble_check = 2
                            break
                        except NoSuchElementException:
                            pass

                        print(f'verificando se as especificações do sku está marcada para : {cod_nome_sku}')
                        linha_sku_names = driver.find_elements(By.TAG_NAME,'label')

                        for e in range(0,len(linha_sku_names)):

                           list_sku_names_text.append(linha_sku_names[e].text)

                        for t in range(0,len(list_sku_names_text)):

                            if list_sku_names_text[t] != '':
                                list_sku_names_text_def.append(list_sku_names_text[t])

                        print(f'{ list_sku_names_text_def}')

                        for h in range(0,len( list_sku_names_text_def)):

                            if list_sku_names_text_def[h] == cod_nome_sku:

                                print(f'{list_sku_names_text_def[h]} encontrado !')
                                patch_nome_sku = '//*[@id="ctl00_Conteudo_ctrlEspecificacao_rptSkuFieldValue_ctl01_radioValor_'+f'{h}'+'"]'
                                print(f'{patch_nome_sku}')
                                nome_sku_selecionado = driver.find_element(By.XPATH,patch_nome_sku)
                                if nome_sku_selecionado.is_selected() == True:
                                    print('o nome sku está correto e selecionado !')
                                    doble_check = 2
                                    break
                                else:
                                    print('selecionando especificação')
                                    nome_sku_selecionado.click()
                                    doble_check =+ 1
                                    break
                            if list_sku_names_text_def[h] == list_sku_names_text_def[len( list_sku_names_text_def) - 1]:

                                print('nome sku não localizado nas especificações !')
                                list_sku_color_error.append(list_sku[i])
                                doble_check = 2
                                break


                        ##patch_nome_sku_li = '//*[@id="ctl00_Conteudo_ctrlEspecificacao_rptSkuFieldValue_ctl01_radioValor"]/li[75]/label'
                        ##patch_nome_sku_li_sup = '//*[@id="ctl00_Conteudo_ctrlEspecificacao_rptSkuFieldValue_ctl01_radioValor_74"]'
                         ##                       '//*[@id="ctl00_Conteudo_ctrlEspecificacao_rptSkuFieldValue_ctl01_radioValor"]/li[75]/label'

                       ## if nome_sku_selecionado.is_selected() == True :
                        ##    print('o nome sku está correto !')
                        ##    break
                     ##   else :
                        ##    nome_sku_selecionado.click()
                        ##    doble_check =+ 1



                except NoSuchElementException:
                    print('nome sku não localizado nas especificações !')
                    list_sku_color_error.append(list_sku[i])


                    pass

                driver.find_element(By.XPATH, '//*[@id="skuTabNavigation"]/li[1]/a').click()

                if sku_ativo.is_selected() == 1:
                    pass
                elif sku_ativo_box.is_selected() == 0:
                    sku_ativo_box.click()

                driver.find_element(By.XPATH,'//*[@id="ctl00_Conteudo_BtnSalvar"]').click()



            espera_linha_sku = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id,"ctl00_Conteudo_rptSku__rli")]')))
            print(espera_linha_sku)
            linha_de_sku = driver.find_elements(By.XPATH, ('//*[contains(@id,"ctl00_Conteudo_rptSku__rli")]'))
            print(str(len(linha_de_sku)) + ' linhas de sku')
            print('estou procurando o : '+ cod_ref)
            espera(1,1)
            for k in range(0,len(linha_de_sku)):
                patch_status_sku_line = '//*[@id="ctl00_Conteudo_rptSku__rli'+str(k)+'"]/table/tbody/tr/td[2]/table/tbody/tr/td[3]'
                status_sku_line = driver.find_element(By.XPATH,patch_status_sku_line).text
                status_sku_line = status_sku_line[5:]
                print(status_sku_line)
                if status_sku_line == cod_ref:
                    espera(1,1)
                    patch_status_sku = '//*[@id="ctl00_Conteudo_rptSku__rli'+str(k)+'"]/table/tbody/tr/td[2]/table/tbody/tr/td[5]/span'
                    espera(1,1)
                    status_sku = driver.find_element(By.XPATH,patch_status_sku).text
                    break

            print(status_sku)

            if status_sku == 'Ativa':
                list_sku_ok.append(list_sku[i])
                print('sku esta ativo')
                up_paste = list_caminho[i][:-14] + list_caminho[i][-9:]
                print(up_paste)
                os.rename(f"{list_caminho[i]}",f"{up_paste}")
            else :
                print("Inativa")
                list_inativo.append(list_sku[i])

            if verif_stoque(sku) == True:
                print(f'o produto {sku} tem estoque')

            else:
                print(f'o produto {sku} não tem estoque')
                list_sem_estoque.append(list_sku[i])

            if verif_preco(sku,cod_nome_sku) == False:
                print(f'o produto {sku} não tem preço')
                list_sem_preco.append(list_sku[i])
            else:
                print(f'o produto {sku} tem preço')


            status_sku = 0
            linha_de_sku.clear()



        if len(list_sku_ok) != 0:

            print("\n\n\n|**********|\n Sku's Ativos\n")

            for i in range(0,len(list_sku_ok)):
                print('  '+str(list_sku_ok[i]))

            print("\n|**********|")
            print("\n Num Sku's : " + str(len(list_sku_ok)))

        if len(list_inativo) != 0:

            print("\n\n\n|***************|\n Sku's inativos\n")

            for i in range(0,len(list_inativo)):
                print('      '+str(list_inativo[i]))
            print("\n Num Sku's : "+str(len(list_inativo)))

            print("\n|***************|")

        if len(list_img_format_error) != 0:

            print("\n\n\n|*****************|\n Sku's img format\n")

            for i in range(0,len(list_img_format_error)):
                print('      '+str(list_img_format_error[i]))
            print("\n Num Sku's : "+str(len(list_img_format_error)))

            print("\n|*****************|")

        if len(list_sku_number_error) != 0:

            print("\n\n\n|******************|\n Sku's number error\n")

            for i in range(0, len(list_sku_number_error)):
                print('      ' + str(list_sku_number_error[i]))
            print("\n Num Sku's : " + str(len(list_sku_number_error)))

            print("|******************|")

        if len(list_sku_color_error) != 0:

            print("\n\n\n|**************|\n Sku's Color error\n")

            for i in range(0, len(list_sku_color_error)):
                print('      ' + str(list_sku_color_error[i]))
            print("\n Num Sku's : " + str(len(list_sku_color_error)))

            print("\n|**************|")

        if len(list_sem_estoque) != 0:

            print("\n\n\n|*****************|\n Sku's sem estoque\n")

            for i in range(0,len(list_sem_estoque)):
                print('      '+str(list_sem_estoque[i]))
            print("\n Num Sku's : "+str(len(list_sem_estoque)))

            print("\n|*****************|")

        if len(list_sem_preco) != 0:

            print("\n\n\n|**************|\n Sku's sem preço\n")

            for i in range(0,len(list_sem_preco)):
                print('      '+str(list_sem_preco[i]))
            print("\n Num Sku's : "+str(len(list_sem_preco)))

            print("\n|**************|")

        if len(list_manual) != 0:

            print("\n\n\n|**************|\n Sku's manual\n")

            for i in range(0,len(list_manual)):
                print('      '+str(list_manual[i]))
            print("\n Num Sku's : "+str(len(list_manual)))

            print("\n|**************|")

        driver.quit()

        if selecao == 'all':
            check = True


    return print("executado")



if __name__ == '__main__':
    upador()

