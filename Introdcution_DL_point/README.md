# 핵심 딥러닝 입문: RNN, LSTM, GRU, VAE, GAN 구현

![image](https://user-images.githubusercontent.com/40276516/101937110-c5cd7e00-3c24-11eb-91a3-46a1a7128d22.png)

## 딥러닝 기술

### RNN
RNN (Recurrent Neural Network): 일반적인 신경망에 시간 방향으로의 연결 개념을 적용
<br>
LSTM : 내부에 '게이트'와 '기억 셀'이라는 구조를 갖는 발전된 형태의 RNN
<br>
GPU : 기억 셀이 없어 상대적으로 간단한 구조의 LSTM

### 생성 모델
VAE (Variational Auto Encoder) : 데이터의 특징을 몇 개의 잠재 변수로 압축하고 복원
<br>
GAN (Generative Adversarial Networks) : 가짜를 만들어내는 생성자와 가짜를 식별하는 식별자가 서로 경쟁하도록 학습시켜 실제와 똑같은 데이터를 생성
