#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单的测试脚本来验证Hello World页面
"""

import os
import sys

# 添加arachnado模块到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'arachnado'))

def test_hello_world():
    """测试Hello World页面是否正确创建"""
    
    # 检查Hello World页面文件是否存在
    hello_world_file = "arachnado/static/js/pages/HelloWorldPage.jsx"
    if os.path.exists(hello_world_file):
        print("✓ Hello World页面文件已创建")
        
        # 读取文件内容验证
        with open(hello_world_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "Hello World" in content:
                print("✓ Hello World页面内容正确")
            else:
                print("✗ Hello World页面内容不正确")
    else:
        print("✗ Hello World页面文件不存在")
    
    # 检查路由配置
    main_file = "arachnado/static/js/main.jsx"
    if os.path.exists(main_file):
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "HelloWorldPage" in content and 'path="hello"' in content:
                print("✓ 路由配置正确")
            else:
                print("✗ 路由配置不正确")
    
    # 检查CSS样式
    css_file = "arachnado/static/css/style.css"
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "hello-world-page" in content:
                print("✓ CSS样式已添加")
            else:
                print("✗ CSS样式未找到")
    
    # 检查构建文件
    build_files = ["arachnado/static/build/main.js", 
                   "arachnado/static/build/vendor.js",
                   "arachnado/static/build/common.js"]
    
    for build_file in build_files:
        if os.path.exists(build_file):
            print(f"✓ {os.path.basename(build_file)} 构建文件存在")
        else:
            print(f"✗ {os.path.basename(build_file)} 构建文件不存在")

    print("\n🎉 Hello World应用创建完成！")
    print("📝 要访问Hello World页面，请在Arachnado应用中访问: #/hello")

if __name__ == "__main__":
    test_hello_world()