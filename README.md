# CompressionData
The training data of learned image compression. The data is from flicker.com.
You can download the data in from [link](https://bhpan.buaa.edu.cn:443/link/5A49A835629D57929F82A2D97A6EC855).
We update the Google Drive download [link](https://drive.google.com/file/d/1EK04NO6o3zbcFv5G-vtPDEkPB1dWblEF/view?usp=sharing).
Then you can generate the 256*256 patches using following script.
```
python generatePatchFlickr.py flicker_2W_images/ output_path/
```
The size of output training dataset is over 80G.


If your find our dataset is helpful for your research, please cite our paper.
Besides, our dataset is only for research use.
```
@article{liu2020unified,
  title={A Unified End-to-End Framework for Efficient Deep Image Compression},
  author={Liu, Jiaheng and Lu, Guo and Hu, Zhihao and Xu, Dong},
  journal={arXiv preprint arXiv:2002.03370},
  year={2020}
}
