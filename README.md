# auto_click.py


先到尚未開賣的網頁，前一分鐘執行此程式，會自動刷新並且購物。
ps.我遇到購物車是空的無法購買問題

![image](https://user-images.githubusercontent.com/54543570/157814001-e42c5017-ec76-479f-baef-59ec535040a0.png)


# credict_card.py

![image](https://user-images.githubusercontent.com/54543570/157814284-79497590-b078-4634-82aa-6adfb86bce10.png)


步驟3也可以用程式碼解決，但是怕網頁跳轉太慢會失敗，可以用

` 
WebDriverWait(driver, 1, 0.2).until(
            EC.presence_of_element_located((By.ID, 'buy_yes'))
        )
` 

方式去解決，要抓什麼ID就可用檢查去查看

只要改信用卡號碼較可以搶購了，以上方式祝大家搶購成功
