# 天气查询程序

一个简单易用的命令行天气查询工具，使用 Python 编写。

## 功能特点

- 🌍 支持全球城市天气查询
- 🌡️ 显示当前温度、湿度、风速等信息
- 📅 支持未来多天天气预报
- 🔑 无需 API key，使用免费的 wttr.in 服务
- 📝 简洁的命令行界面

## 依赖要求

- Python 3.6+

## 使用方法

### 查询当前天气

```bash
python weather.py [城市名]
```

示例：
```bash
# 查询北京天气（默认）
python weather.py

# 查询上海天气
python weather.py Shanghai

# 查询东京天气
python weather.py Tokyo
```

### 查询天气预报

```bash
python weather.py [城市名] -f
```

### 指定预报天数

```bash
# 查询未来5天天气预报
python weather.py Shanghai -f -d 5
```

### 帮助信息

```bash
python weather.py -h
```

## 支持的城市名称

可以使用中文拼音、英文名称或 IATA 机场代码：
- Beijing, Shanghai, Guangzhou, Shenzhen
- Tokyo, London, New York, Paris
- 以及全球任何主要城市

## 示例输出

```
📍 BEIJING - 当前天气
========================================
🌡️  温度: 22°C (72°F)
☁️  天气: 晴朗
💨 风速: 12 km/h
💧 湿度: 45%
🌅 日出: 06:15 AM
🌇 日落: 06:45 PM
```

## 技术说明

- 使用 [wttr.in](https://wttr.in) 提供的免费天气 API
- 数据来源：世界气象组织
- 无需注册或 API key

## 许可证

MIT License
