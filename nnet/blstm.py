import torch
import torch.nn as nn
import torch.nn.functional as F

# 定义BiLSTM的结构
class blstm(nn.Module):
    def __init__(self, INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE, LAYERS, DROP_RATE):
        super(blstm, self).__init__()
        
        self.rnn = nn.LSTM(
            input_size = INPUT_SIZE, 
            hidden_size = HIDDEN_SIZE, 
            num_layers = LAYERS,
            dropout = DROP_RATE,
            batch_first = True,     # 如果为True，输入输出数据格式是(batch, seq_len, feature)
            bidirectional=True      # 双向
        )
        self.output = nn.Linear(2 * HIDDEN_SIZE, OUTPUT_SIZE)  # 最后一个时序的输出接一个全连接层
        self.h_s = None
        self.h_c = None

    def forward(self, frames_batch):
        r_out, (h_s, h_c) = self.rnn(frames_batch)      # 如果不导入h_s和h_c，默认每次都进行0初始化
                                                        # h_s和h_c表示每一个隐层的上一时间点输出值和输入细胞状态
                                                        # h_s和h_c的格式均是(num_layers * num_directions, batch, HIDDEN_SIZE)
                                                        # 如果是双向LSTM，num_directions是2，单向是1
        out = self.output(r_out)
        # out_prob = F.softmax(out, dim=1)
        return out