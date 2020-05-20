# CompressionData
The training data of learned image compression. The data is from flicker.com.
You can download the data in [link](https://bhpan.buaa.edu.cn:443/link/5A49A835629D57929F82A2D97A6EC855).
Then you can generate the 256*256 patches using following script.
```
python generatePatchFlickr.py flicker_2W_images/ output_path/
```
The size of output training dataset is over 80G.
