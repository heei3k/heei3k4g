https://zhuanlan.zhihu.com/p/555114726

Allure监听器在测试执行期间会收集结果，只需添加alluredir选项，并选择输出的文件路径即可。
pytest --alluredir=./allure-results

# 执行此命令，将在默认浏览器中显示生成的报告
allure serve ./allure-results