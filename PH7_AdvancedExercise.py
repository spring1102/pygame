#输入数字输出对应的英语
#目前只有0-10
def printNumInEng(num):
    EnglishList = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
    print(EnglishList[num])
while True:
    num = input("Enter the integer(0-10):")
    num = int(num)
    printNumInEng(num)