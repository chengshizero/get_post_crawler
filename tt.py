
def single(): 
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import jieba
    text_from_file_with_apath = open('tt.txt',encoding='utf-8').read()
	 
    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
    wl_space_split = " ".join(wordlist_after_jieba)
    font = 'C:/Windows/Fonts/simfang.ttf'
    my_wordcloud = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(wl_space_split)
	 
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()

def pic():
    from PIL import Image
    from wordcloud import WordCloud, ImageColorGenerator
    import matplotlib.pyplot as plt
    import numpy as np
    import jieba
    path_txt = 'tt.txt'
    path_img = "tt.jpg"
    f = open(path_txt, 'r', encoding='UTF-8').read()
    background_image = np.array(Image.open(path_img))
    # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云,感兴趣的朋友可以去查一下，有多种分词模式
    #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    cut_text = " ".join(jieba.cut(f))

    wordcloud = WordCloud(
    # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    font_path="C:/Windows/Fonts/simfang.ttf",
    background_color="white",
    # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
    mask=background_image).generate(cut_text)
    # 生成颜色值
    image_colors = ImageColorGenerator(background_image)
    # 下面代码表示显示图片
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.show()
	
if __name__ == '__main__':
    single()
    pic()