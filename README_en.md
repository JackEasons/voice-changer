## VC Helper

# What is VC Helper

[VC Helper](https://github.com/w-okada/voice-changer) is a client software for real-time voice changers that uses AI such as [MMVC](https://github.com/isletennos/MMVC_Trainer) and [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc). It also provides an app for recording training audio for real-time voice changers, specifically for MMVC.

- Please use the [official notebook](https://github.com/isletennos/MMVC_Trainer) for MMVC training.
- Please use the [official notebook](https://github.com/isletennos/MMVC_Trainer) for so-vits-svc training.

# Features

1. Cross-platform compatibility
   Supports Windows, Mac (including Apple Silicon M1), Linux, and Google Colaboratory.

2. No need to install a separate audio recording app
   Audio recording can be done directly on the application hosted on Github Pages. Since it runs entirely on the browser, there is no need to install any special application. Additionally, since it works entirely as a browser application, no data is sent to the server.

3. Distribute the load by running Voice Changer on a different PC
   The real-time voice changer of this application works on a server-client configuration. By running the MMVC server on a separate PC, you can run it while minimizing the impact on other resource-intensive processes such as gaming commentary.

![image](https://user-images.githubusercontent.com/48346627/206640768-53f6052d-0a96-403b-a06c-6714a0b7471d.png)

# usage

Details are summarized [here](https://zenn.dev/wok/books/0004_vc-helper-v_1_5_1_x).

# (1) Recorder (Voice Recording App for Training)

This is an app that allows you to easily record training voice for MMVC. It can be run on Github Pages, making it available from various platforms with just a browser. The recorded data is saved in the browser and will not leak externally.

[Recorder app on Github Pages](https://w-okada.github.io/voice-changer/)

[Explanation video](https://youtu.be/s_GirFEGvaA)

# (2) Player (Voice Changer App)

This is an app for performing voice changes with MMVC and so-vits-svc.

It can be used in three main ways, in order of difficulty:

- Using Google Colaboratory (MMVC only)
- Using a pre-built binary
- Setting up an environment with Docker or Anaconda and using it

For those who are not familiar with this software or MMVC, it is recommended to gradually get used to it from the top.

## (2-1) Use on Google Colaboratory (MMVC only)

You can run it on Google's machine learning platform, Colaboratory. If you have already used Colaboratory, you do not need to prepare anything as the training of MMVC model has been completed. However, the voice changer may have a large time lag depending on the network environment or the situation of Colaboratory.

- [Simple version](https://github.com/w-okada/voice-changer/blob/master/VoiceChangerDemo_Simple.ipynb): You can run it from Colab without any prior setup.
- [Normal version](https://github.com/w-okada/voice-changer/blob/master/VoiceChangerDemo.ipynb): You can load the model by cooperating with Google Drive.

[Explanation video](https://youtu.be/TogfMzXH1T0)

## (2-2) Usage with pre-built binaries

You can download and run the executable binary file.
Both Windows and Mac versions are available.

- For Mac version, after extracting the downloaded file, double-click on `startHttp_xxx.command` corresponding to the VC you want to use. If you are prompted with a message saying that the developer cannot be verified, press the Control key and click again to execute (or right-click to execute). (See details below \*1)

- For Windows version, ONNX version and ONNX+PyTorch version are provided. Download the zip file corresponding to your environment, extract it, and then execute `start_http_xxx.bat` corresponding to the VC you want to use.

・The following voice changers can be started using the various `startHttp_xxx.command` files (Mac) and `start_http_xxx.bat` files (Windows):

| #   | Batch File                                | Description                                 |
| --- | ----------------------------------------- | ------------------------------------------- |
| 1   | start_http_v13.bat                        | Can use MMVC v.1.3.x models.                |
| 2   | start_http_v15.bat                        | Can use MMVC v.1.5.x models.                |
| 3   | start_http_so-vits-svc_40.bat             | Can use so-vits-svc 4.0 models.             |
| 4   | start_http_so-vits-svc_40v2.bat           | Can use so-vits-svc 4.0v2 models.           |
| 5   | start_http_so-vits-svc_40v2_tsukuyomi.bat | Use Tsukuyomi-chan's model. (cannot change) |

・If connecting remotely, use the files with https instead of http in their names for Mac (.command) and Windows (.bat).

・If you have an Nvidia GPU, it will usually work with the ONNX version. However, in rare cases, the GPU may not be recognized. In that case, please use the ONNX+PyTorch(cuda) version (the size is significantly different).

・If you do not have an Nvidia GPU, the ONNX(DirectML) version will usually work.

・For the operation of so-vits-svc and Tsukuyomi-chan, a content vec model is required. Download the ContentVec_legacy 500 model from this [repository](https://github.com/auspicious3000/contentvec) and place it in the same folder as the `startHttp_xxx.command` or `start_http_xxx.bat` that you will execute.
| Version | OS | Framework | Link | VC Support | Size |
| --------- | ------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------ |
| v.1.5.1.7 | mac(M1) | ONNX(cpu) | [Normal](https://drive.google.com/file/d/1SVTwIHYoniYYAGU6Kw6NnS1IE07NgSMd/view?usp=sharing) | MMVC v.1.5.x, MMVC v.1.3.x, so-vits-svc 4.0v2 | 571MB |
| | | | [Tsukuyo Michan](https://drive.google.com/file/d/1s2IYsGST_TqGiOBkVWE5e7wLPfWQf1sY/view?usp=sharing) | so-vits-svc 4.0v2 | 949MB |
| | windows | ONNX(cpu,cuda),PyTorch(cpu) | [Normal](https://drive.google.com/file/d/191vw7_9wF2sba4SofOaNov3f9QmMkjIb/view?usp=sharing) | MMVC v.1.5.x, MMVC v.1.3.x | 597MB |
| | | | [Tsukuyo Michan](https://drive.google.com/file/d/19kNfGk9j3z15IuEZZn9_lmxyDd1_UjoI/view?usp=sharing) | so-vits-svc 4.0v2 | 703MB |
| | | ONNX(cpu,cuda), PyTorch(cpu,cuda) | [Normal](https://drive.google.com/file/d/1_fK-U5odfk9MukMmjwWCsnBNicQcshJv/view?usp=sharing) | MMVC v.1.5.x, MMVC v.1.3.x, so-vits-svc 4.0v2| 2.6GB |
| | | ONNX(cpu,DirectML), PyTorch(cpu) | [Normal](https://drive.google.com/file/d/1iHEC-p6mVLgDCMnWaFg3-dZfuO8njRci/view?usp=sharing) | MMVC v.1.5.x, MMVC v.1.3.x | 462MB |
| | | ONNX(cpu,DirectML), PyTorch(cpu,cuda)| [Normal](https://drive.google.com/file/d/1a9ChdXb7e-LVIuiDDMyVU0oKDhxhZhIT/view?usp=sharing) | MMVC v.1.5.x, MMVC v.1.3.x | 2.48GB |

\*1 MMVC v.1.5.x is Experimental.

\*2 Tsukuyo Michan uses free character "Tsukuyo Michan" voice data that is publicly available for free. (Details such as terms of use are at the end of the document)

https://user-images.githubusercontent.com/48346627/212569645-e30b7f4e-079d-4504-8cf8-7816c5f40b00.mp4

\*3 This software is not signed by the developer. A warning message will appear, but you can run the software by clicking the icon while holding down the control key. This is due to Apple's security policy. Running the software is at your own risk.

![image](https://user-images.githubusercontent.com/48346627/212567711-c4a8d599-e24c-4fa3-8145-a5df7211f023.png)

## (2-3) Usage after setting up the environment such as Docker or Anaconda

Clone this repository and use it. Setting up WSL2 is essential for Windows. Additionally, setting up virtual environments such as Docker or Anaconda on WSL2 is also required. On Mac, setting up Python virtual environments such as Anaconda is necessary. Although preparation is required, this method works the fastest in many environments. **<font color="red"> Even without a GPU, it may work well enough with a reasonably new CPU </font>(refer to the section on real-time performance below)**.

[Explanation video on installing WSL2 and Docker](https://youtu.be/POo_Cg0eFMU)

[Explanation video on installing WSL2 and Anaconda](https://youtu.be/fba9Zhsukqw)

## Real-time performance

Conversion is almost instantaneous when using GPU.

https://twitter.com/DannadoriYellow/status/1613483372579545088?s=20&t=7CLD79h1F3dfKiTb7M8RUQ

Even with CPU, recent ones can perform conversions at a reasonable speed.

https://twitter.com/DannadoriYellow/status/1613553862773997569?s=20&t=7CLD79h1F3dfKiTb7M8RUQ

With an old CPU (i7-4770), it takes about 1000 msec for conversion.

# Acknowledgments

- Tachizunda-mon materials: https://seiga.nicovideo.jp/seiga/im10792934
- Irasutoya: https://www.irasutoya.com/
- Tsukuyomi-chan

> This software uses the voice data of the free material character "Tsukuyomi-chan," which is provided for free by CV. Yumesaki Rei.
>
> - Tsukuyomi-chan Corpus (CV. Yumesaki Rei)
>
> https://tyc.rei-yumesaki.net/material/corpus/
>
> Copyright. Rei Yumesaki

# Terms of Use

Regarding the Real-time Voice Changer Tsukuyomi-chan, we prohibit the following uses in accordance with the terms of use of the Tsukuyomi-chan Corpus.

- Criticizing or attacking individuals (the definition of "criticizing or attacking" is based on the Tsukuyomi-chan character license).

- Advocating for or opposing specific political positions, religions, or ideologies.

- Publicly displaying strongly stimulating expressions without proper zoning.

- Publicly disclosing secondary use (use as materials) for others.
  (Distributing or selling as a work for viewing is not a problem.)

# Disclaimer

We are not liable for any direct, indirect, consequential, incidental, or special damages arising out of or in any way connected with the use or inability to use this software.