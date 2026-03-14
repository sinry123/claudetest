#!/usr/bin/env python3
"""
天气查询程序
使用 wttr.in API 获取天气信息，无需 API key
"""

import argparse
import sys
from urllib.request import urlopen
from urllib.error import URLError
import json


def get_weather(location, format_type="current"):
    """获取指定地点的天气信息"""
    base_url = "https://wttr.in"

    if format_type == "current":
        # 获取当前天气（JSON格式）
        url = f"{base_url}/{location}?format=j1"
    else:
        # 获取详细预报
        url = f"{base_url}/{location}?format=j1"

    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        return data
    except URLError as e:
        print(f"错误: 无法获取天气信息 - {e}")
        sys.exit(1)


def display_current_weather(data, location):
    """显示当前天气"""
    current = data['current_condition'][0]

    print(f"\n📍 {location.upper()} - 当前天气")
    print("=" * 40)
    print(f"🌡️  温度: {current['temp_C']}°C ({current['temp_F']}°F)")
    print(f"☁️  天气: {current['weatherDesc'][0]['value']}")
    print(f"💨 风速: {current['windspeedKmph']} km/h")
    print(f"💧 湿度: {current['humidity']}%")
    print(f"🌅 日出: {data['weather'][0]['astronomy'][0]['sunrise']}")
    print(f"🌇 日落: {data['weather'][0]['astronomy'][0]['sunset']}")
    print()


def display_forecast(data, location, days=3):
    """显示天气预报"""
    print(f"\n📍 {location.upper()} - 未来{days}天预报")
    print("=" * 40)

    for day in data['weather'][:days]:
        print(f"\n📅 {day['date']}")
        print(f"   最高: {day['maxtempC']}°C  最低: {day['mintempC']}°C")
        print(f"   ☁️  {day['hourly'][0]['weatherDesc'][0]['value']}")
        print(f"   💨 风速: {day['hourly'][0]['windspeedKmph']} km/h")
        print(f"   💧 降雨概率: {day['hourly'][0]['chanceofrain']}%")


def main():
    parser = argparse.ArgumentParser(description="天气查询程序")
    parser.add_argument("location", nargs="?", default="Beijing",
                       help="查询地点 (默认: Beijing)")
    parser.add_argument("-f", "--forecast", action="store_true",
                       help="显示未来3天天气预报")
    parser.add_argument("-d", "--days", type=int, default=3,
                       help="预报天数 (默认: 3)")

    args = parser.parse_args()

    # 获取天气数据
    weather_data = get_weather(args.location)

    # 显示天气信息
    display_current_weather(weather_data, args.location)

    if args.forecast:
        display_forecast(weather_data, args.location, args.days)


if __name__ == "__main__":
    main()
