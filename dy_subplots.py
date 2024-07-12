# 迴圈呼叫 plotSeams 並動態增加子圖
    # 計算要分成幾行幾列
    num_plots = len(qdvp)
    num_cols = 5  # 假設每行最多 n 個子圖
    num_rows = (num_plots // num_cols)  # 向上取整

    # fig = plt.figure(figsize=(12, 12))

    # for i in range(1, 10):
    #     ax = fig.add_subplot(3, 3, i, projection='3d')

    fig = plt.figure()
    axs = fig.add_subplot(num_cols, num_rows ,9 , projection='3d')#, sharex=True, sharey=True)
    # fig, axs = plt.subplots(nrows=num_rows, ncols=num_cols, sharex=True, sharey=True)
    plt.title('Seam-Shift')
            
    for i_pt in range(num_plots):
        if i_pt == 10:
            break
        # axs[i_pt] = qdvp[i_pt]
        # plt.gca().set_title('Plot %d' % (i_pt))
        # plt.axis('off')  # 可以關閉子圖的坐標軸
        
        fig.add_subplot(axs[i_pt])
        # plt.sca(ax)
                

    plt.tight_layout()  # 自動調整子圖間距
    plt.show()
