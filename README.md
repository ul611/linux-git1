## Linux_features_42tests

_Некоторые особенности написания кода и запуска популярных юнит-тестов проектов Libft, Get Next Line, Ft_printf, Libft, Libft, Libft, Get Next Line, Ft_printf, Libft, Get Next Line, Ft_printf на Linux._

**0.** Некоторые man на MacOS отличаются от man на Linux. В основном, отличия незначительны, 
но лучше гуглить "man macOS <функция>", чтобы ничего не упустить (или не сделать лишнего).

Например, в функции calloc() для Linux указано дополнительное ограничение на максимальный
размер выделяемой памяти (If the multiplication of nmemb and size would result in integer 
overflow, then calloc() returns an error), чего нет в мануале для Mac.

Первая ссылка в гугле будет выглядеть примерно так:
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/calloc.3.html

### Проекты.

#### 1. Libft

**1.1.** 	https://github.com/jtoty/Libftest
		
		Максимально дружелюбный тест.

**1.2.**	https://github.com/alelievr/libft-unit-test
		
		для данного теста:
		
		- добавляем правило so в Makefile (его не обязательно удалять перед сдачей проекта),
		например, такое:
		
		so:			$(OBJS) $(OBJSBONUS) $(HDR)
					gcc -fPIC $(FLAGS) -c $(SRCSBONUS) $(SRCS)
					gcc -shared -o libft.so $(OBJS) $(OBJSBONUS)
		
		- устанавливаем пакеты clang, build-essential, autoconf, libncurses-dev, libbsd-dev.
		
**1.3.**	Стандартно стоит проверить проект на утечки, например, при помощи valgrind
		
		Стоит иметь в виду, что прохождение данных тестов не может гарантировать успешной сдачи либы.
		
		Спойлер: как Мулинетт, так и тесты, очень поверхностно проверяют бонусную часть. 


#### 2. Get next line
