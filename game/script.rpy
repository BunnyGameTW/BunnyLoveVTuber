﻿define b = Character('小兔子', color="#7aea7a")
define y = Character('Yto', color="#f3e272")

image milk:
    "milk.png"
    subpixel True
    size (1280, 720)
    xalign .5
    yalign .5
    crop (500, 500, 590, 332)
    easein 5.0 crop (0,0,1920,1080)
# 遊戲從這裡開始。
label start:
    scene bg forest with fade
    "從前從前，有一隻小兔子住在森林裡，過著她的兔生"
    scene bg house with dissolve
    "這天，她一如往常的結束了她的攻城部作業後，躺在床上滑著免書"
    scene bg fb with dissolve
    "突然間，她滑到了一個影片 - Gura唱bubbly讓我融化了"
    b "好像常常看到這個叫做Gura的人，到底是什麼？有這麼好聽嗎？"
    menu:
        "點下去看看？"
        "好":
            $ renpy.movie_cutscene("video/gura.webm")
            b "我的媽，是天使!天使下凡了!"
            b "嗯...？"
            "歪踢的自動撥放功能推薦下部影片 - 死神與Gura邊玩瑪李歐賽車邊互罵"
            b "好像很有趣，來看看"
            "..."
            b "這個粉毛也太好笑，聲音也好讚，發音也好清楚，我英文那麼差還聽得懂耶"
            b "嗯...森美聲？ 這名字也太奇怪，她到底是四本還是米國人，來噗狗看看"
            "小兔子就這樣找著找著，發現原來這些人叫做VTuber，用虛擬形象做許多有趣的直播等等"
            "她們有趣的互動、充實的內容讓小兔子跌進了兔子洞，進而發現還有所謂的fan art"

            b "要是我也能做點什麼就好了... 咦，之前不是看到有個blender建模軟體，來試試看照著教學做點東西吧!"#blender
            menu:
                "做做看？"
                "來吧":
                    scene black with dissolve
                    pause(2.0)
                    play sound "audio/win.mp3"
                    scene milk with fade
                    b "呼，完成了!雖然還很陽春，試著上傳給大家看看!"
                    scene bg twitter with dissolve
                    "隔天，她打開凸特發現，有超過一個人幫她按愛心，她開心到後空翻(?)"
                    
                    b "喔喔喔!好棒!有人喜歡!"
                    b "邊看直播還能邊學東西，好像很棒耶!這就是創作的快樂嗎？自從加入攻城部隊後好像沒有過這種激動的感覺了!"
                    "於是小兔子除了Calli之外也漸漸會開始看其他VT，不知不覺就變成了DD"

                    scene bg hole with dissolve
                    "有天他發現叫做Yto的同學竟然一樣在兔洞裡，並向她推薦一個有許多跟她一樣興趣的俱樂部"
                    y "我跟你說，fuwaClub超讚，我每天在裡面學到一堆，只是我都用偷看的，欸嘿(//w//)"
                    b "但是我好爛耶，我有辦法加入嗎(つAC)"
                    y "可以的!要對自己有信心!妳我一起加油q(o`w`o)p"
                    "小兔子拿出向梁靜借來的勇氣詢問了是否能加入俱樂部"
                    scene black with dissolve

                    #black doki doki
                    stop music fadeout 0.5
                    play sound "audio/heartbeat.wav"
                    "..."
                    play sound "audio/heartbeat.wav"
                    "....."
                    play sound "audio/heartbeat.wav"
                    "......."
                    #se yatta   
                    play sound "audio/win.mp3"
                    scene bg ending_3 with dissolve
                    b "通過了!好耶!考兔國大學都沒這麼緊張..."
                    #scene good ending!
                    play sound "audio/yatta.mp3"
                    "在加入fuwaClub後，小兔子漸漸找回了做遊戲的熱情，是因為有大家的溫暖，她才能繼續努力下去"
                    play sound "audio/ending.mp3"
                    "從此以後小兔子過著快樂創作的看V兔生，可喜可賀、可喜可賀!"

                    if (persistent.showGallery is None) or (persistent.showGallery == False):
                        $ renpy.notify("解鎖了畫廊！")
                        $ persistent.showGallery = True

                    call showEnding("快樂創作的看V兔生") from _call_showEnding_1
                "好麻煩喔":
                    stop music fadeout 0.5
                    scene bg ending_2 with dissolve
                    play sound "audio/normalEnd.mp3"
                    "小兔子雖然很愛看V，但她老是覺得提不起勁，日復一日、年復一年，她過著覺得有點累的看V兔生"
                    call showEnding("累累的看V兔生") from _call_showEnding_2
        "不要好了":
            stop music fadeout 0.5
            scene bg ending_1 with dissolve
            play sound "audio/badEnd.mp3"
            "小兔子沒興致地繼續滑著免書，日復一日年復一年，過著平凡無奇的兔生"
            call showEnding("平凡無奇的兔生") from _call_showEnding
    return

label showEnding(e):
    "達成了結局[e]"
    return


