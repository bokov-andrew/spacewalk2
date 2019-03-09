# Escape game add-ons
# version 0.0.1
#
# Here are some functions that can be helpful to people who are
# working through the excellent book called "Mission Python
# Code a Space Adventure Game!" by Sean McManus, copyright 2018
#
# This code is open source, distributed free of charge, and is
# not a product of No Starch Press. The authors are not
# affiliated with No Starch Press or Sean McManus
#
# In other words, do not bother Mr. McManus if you find bugs
# in our code, he did not write this script.

# In chapter 5, pp 88,91-94 there is a huge dictionary named
# objects with 80 objects in it, indexed by number. It will
# be tedious for young students to type, and difficult even
# for experienced programmers to remember what each number
# represents. This function lets you pull the object you want
# out of that list by referring to its image. The arguments
# are as follows:
#
# oname:    the name of the object (string)
# obj:      the objects variable (currently, list)
# whichone: if the same image is used more than once, it lets
#           you select which one of them you get back. It's an
#           optional argument with a default value of 0 so if
#           you leave it out you will get the first instance of
#           it which is usually what you need.
#
# Example: gt('floor',DEMO_OBJECTS)
# ...returns the floor item from that list.
#
# Warning: we're about to get to the objects section, but we're
# not quite there yet, so we're using DEMO_OBJECTS in this
# version, just to test things out. This function won't work
# with the real objects dictionary. We will modify it and
# release a new version when we get to that part of the book.
def get_prop(oname,obj=None,img=None,whichone=0,val=True,env=None):
    if env:
        if not img: img = env['images']
        if not obj: obj = env['objects']
    oo = [[kk,vv] for kk,vv in obj.items() if vv[0] == img.__getattr__(oname)]
    if len(oo) == 1: oo = oo[0]
    else: oo = oo[whichone]
    if val: return oo[1]
    else: return oo[0]
    
