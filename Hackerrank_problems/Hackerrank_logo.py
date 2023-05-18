width = int(input())
logo = 'H'

#Top Cone
for i in range(width):
    # top_cone = (logo * i).rjust(width - 1)
    # left_cone =   (logo * i).ljust(width - 1)
    top_cone = (logo * i).rjust(width-1) + logo + (logo * i).ljust(width - 1)
    print(top_cone)

    # '*' * 0 right 4 spaces print + logo + '*' * 0 left 4 space )

# Top Pillar :
for i in range(width + 1):
    center = (logo * width).center(width * 2) + (" " * width * 2 ) + (logo * width).center(width * 2)
    print(center)

# Mid Tier
for i in range((width + 1)//2):
    mid = (logo * width * 5).center(width * 6)
    print(mid)

# Down pilllar:
for i in range(width + 1):
    center = (logo * width).center(width * 2) + (" " * width * 2 ) + (logo * width).center(width * 2)
    print(center)

#Down cone
for i in range(width):
    down_cone = ((logo * (width - i - 1)).rjust(width) + logo + ((logo * (width - i - 1)).ljust(width))).rjust(width*6)
    print(down_cone)































































#Replace all ______ with rjust, ljust or center.

# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
#
