# Chainlit GPT-4 MCP 示例

这个示例展示了如何使用 Chainlit 和 GPT-4 实现 MCP（Model Control Protocol）工具调用功能。

## 功能特点

- 使用 GPT-4 作为对话模型
- 实现了基本的工具调用功能（天气查询示例）
- 展示了如何集成 MCP 工具到对话流程中

## 安装

1. 确保已安装所有依赖：
```bash
pip install -r requirements.txt
```

2. 设置 OpenAI API 密钥：
```bash
export OPENAI_API_KEY='your-api-key'
```

## 运行

使用以下命令启动应用：
```bash
chainlit run app.py
```

## 使用说明

1. 启动应用后，在浏览器中打开显示的地址
2. 在聊天界面中，你可以询问天气信息，例如：
   - "北京天气怎么样？"
   - "上海今天天气如何？"

系统会自动调用天气工具来获取信息并返回结果。

## 注意事项

- 这是一个示例实现，天气信息是模拟的
- 确保你有有效的 OpenAI API 密钥
- 需要 Python 3.8 或更高版本
