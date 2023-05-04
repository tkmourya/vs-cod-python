
# # # # # my_list=[0]*5
# # # # # for index in range(1,5):
# # # # #     my_list[index]=(index-1)*index
                    
# # # # # print(my_list)
# # # # FHW=open("data.txt","w")
# # # # FHW.write("written some thing")
# # # # print(FHW.tell())
# # # # print("closed?",FHW.closed)
# # # # FHW.close()
# # # # print("after closing the file closed?",FHW.closed)
# # # set_1={1,2,3,1,2,4,5,3,4,8,9,7,10}
# # # for index in range(len(set_1)):
# # #     print(index,end=" ")
# # def value(num1):
# #     list1=[]
# #     while num1!=0:
# #         if num1%2==0:
# #             list1.append(num1)
# #         else:
# #             break
# #         num1-=2
# #     print(list1)
# # # value(10) 
# # from email.policy import default


# # def sample(value):
# #     sum1=0
# #     for i in value:
# #         if i%2!=0:
# #             sum1+=value[i]
# #         else:
# #             sum1-=i
# #     print(sum1)
# # dict1={1:2,2:4,3:6,5:8}
# # sample(dict1)
# sample_dict={'a':"apple",'b':"ball"}
# sample_dict.update({'b':"boy", 'c':'cat' })
# print(sample_dict['a'],sample_dict.get('b'),sample_dict.get('c'))
def find_sum(a,b):
    try:
        print(a+c)
    except ValueError:
        print("Function name error")
    finally:
        print("Sum finally")
try:
    find_sum(12,13)
except NameError:
    print("Invocation name error")
finally:
    print("Invocation finally")