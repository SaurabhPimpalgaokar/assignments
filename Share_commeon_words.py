with open("C:\\Users\\141573\\Downloads\\essay.txt","w+") as file_writer:
    file_writer.write("hi hi hi hi ")
    file_writer.write("hello hello hello hello ")
    file_writer.write("i love cricket ")
    file_writer.write("this is my fav game game ")
    file_writer.write("i watch cricket ")
    file_writer.seek(0)
    word_list=[]
    merged_list = []
    while True:
        line = file_writer.readline()
        if not line:
            break
        word_list = line.split(" ")
        merged_list.extend(word_list)
    print(merged_list)
    word_count = 1
    dictionary={}
    for i in merged_list:
        word_count = 1
        for j in merged_list[merged_list.index(i)+1:]:
            if i==j:
                word_count += 1
                merged_list.remove(i)
                dictionary[i] = word_count
            else:
                dictionary[i] = word_count
    print(dictionary)






