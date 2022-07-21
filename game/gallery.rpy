default cgPage = 1

init python:
    import math
    import re
    #const
    CG_COLUMN = 4
    CG_ROW = 1
    TOTAL_CG = 4#TODO set total number
    TOTAL_CG_PAGE = math.ceil(float(TOTAL_CG) / float((CG_COLUMN * CG_ROW)))
    CG_THUMB_SCALE = 0.2
    CG_DATA = [
        [2, "bg fb.png", "bg twitter.png"],
        [1, "bg forest.png"],
        [1, "bg hole.png"],
        [3, "bg ending_1.png", "bg ending_2.png", "bg ending_3.png"],
        #[numbers of images, filename1, filename2, ...]
    ]
    
    #functions
    def cg_thumbnail(finalName, scale):
        return im.FactorScale(finalName, scale, xalign=0.5, yalign=0.5)

    #gallery
    cgga = Gallery()

    for i in range(1, TOTAL_CG + 1):
        cgga.button(i) #this is the name/label associated with your button for a particular image
        for j in range(1, CG_DATA[i - 1][0] + 1):
            cgga.image(CG_DATA[i - 1][j])

    cgga.transition = dissolve


screen cg_button(start, end):
    for (i) in range(start, end + 1):
        if (i <= TOTAL_CG):
            vbox:
                $ the_button = cgga.make_button(i, cg_thumbnail(CG_DATA[i-1][1], CG_THUMB_SCALE))
                add the_button
        else:
            vbox:
                null

screen gallery():    
    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "bg house" at truecenter

    style_prefix "ema"
    vbox:
        ysize 980
  
        label "畫廊":
            ypos 20
            # text_outlines [ (absolute(1), "#3c1717", absolute(1), absolute(2)) ]
            xalign 0.5
            bottom_margin 450
      
        textbutton _("回標題頁面"):
            xpos 60
            action Return()
            bottom_margin 30

        grid CG_COLUMN CG_ROW:
            style_prefix "ema_slot"
            xfill True
            yfill True
            xpos 30
            yspacing 30
            use cg_button((cgPage - 1) * CG_COLUMN * CG_ROW + 1, cgPage * CG_COLUMN * CG_ROW)
