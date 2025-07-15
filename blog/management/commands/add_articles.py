from django.core.management.base import BaseCommand
from blog.models import Article
from django.core.management import call_command
from django.contrib.auth.models import User
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()

        users = CustomUser.objects.all()[:1]
        Article.objects.get_or_create(
                                   title='Обзор флагмана Samsung Galaxy S24 Ultra: идеальный баланс между производительностью и дизайном',
                                   text="""<div class="content-text  muted777">

								
																<div class="introtext_wrapper">
			<div class="introtext">
									<p style="text-align: justify;">Samsung Galaxy S24 Ultra является одним из самых ожидаемых смартфонов этого года. Он был представлен на выставке MWC 2023 как новый флагман компании Samsung. Этот смартфон обещает стать идеальным выбором для тех, кто ищет превосходное сочетание производительности, качества и стиля.</p>							</div>
		</div>
														<p><a href="/catalog/smartfony_i_gadzhety/smartfony_telefony/129982/?oid=129995">Samsung Galaxy S24 Ultra</a> является одним из самых ожидаемых смартфонов этого года. Он был представлен на выставке MWC 2023 как новый флагман компании Samsung. Этот смартфон обещает стать идеальным выбором для тех, кто ищет превосходное сочетание производительности, качества и стиля. В этом обзоре мы рассмотрим все основные характеристики и преимущества Galaxy S24 Ultra, а также сравним его с другими моделями на рынке.</p>
<h2>Дизайн и экран</h2>
<p>Galaxy S24 Ultra имеет элегантный и современный дизайн, который понравится многим пользователям. Корпус смартфона выполнен из высококачественного стекла Gorilla Glass Victus, что обеспечивает ему прочность и долговечность. Размеры устройства составляют 166.9 x 76.7 x 8.4 мм, а вес – 228 грамм. Смартфон оснащен 6,8-дюймовым Super AMOLED Plus экраном с разрешением 1440x3040 пикселей и частотой обновления до 120 Гц. Это обеспечивает яркие, насыщенные цвета и плавное отображение изображения.</p>
<p><img data-lazyload="" class=" lazyloaded" src="/img/2024/23.jpg" data-src="/img/2024/23.jpg" alt="Samsung Galaxy S24 Ultra в блоге Симка" title="Samsung Galaxy S24 Ultra в блоге Симка" style="max-width:100%; max-height:500px;"></p>
<h2>Производительность и память</h2>
<p>В основе Galaxy S24 Ultra лежит процессор Qualcomm Snapdragon 8 Gen 2, который обеспечивает высокую производительность и энергоэффективность. Смартфон имеет 12 ГБ оперативной памяти и поддерживает установку до 512 ГБ внутренней памяти. Также стоит отметить, что устройство поддерживает сети 5G, что позволяет использовать все возможности высокоскоростного интернета.</p>
<h2>Камера и видеосъемка</h2>
<p>На задней панели смартфона расположены четыре основные камеры: 108 МП основная камера с оптической стабилизацией, 32 МП ультраширокоугольная камера, 10 МП телефото камера с трехкратным оптическим зумом и 8 МП камера с датчиком глубины для портретных снимков. Фронтальная камера имеет разрешение 40 МП и позволяет делать качественные селфи и видеозвонки. Galaxy S24 Ultra также поддерживает запись видео в разрешении 8K при 30 кадрах в секунду и 4K при 60 кадрах в секунду.</p>
<h2>Аккумулятор и зарядка</h2>
<p>Смартфон оснащен аккумулятором емкостью 5000 мАч, который обеспечивает длительное время работы устройства без подзарядки. Кроме того, Galaxy S24 Ultra поддерживает быструю зарядку мощностью 65 Вт, что позволяет быстро зарядить аккумулятор.</p>
<h2>Заключение</h2>
<p>Samsung Galaxy S24 Ultra – это один из лучших <a href="/">смартфонов на рынке</a>, который предлагает высокую производительность, стильный дизайн и отличные камеры.</p>			
			</div>""",
                                   image="images_aticle/1.png",
                                   author=users[0],
                                   created_at='2024-01-11 09:49:40.227214+03',
                                   updated_at='2024-01-11 09:49:40.227214+03',
                                   date_published='2024-01-11 09:49:40.227214+03',
                                   published=True,
                                   number_of_views=15)
        Article.objects.get_or_create(
                                      title='Как очистить силиконовый чехол для телефона от потемнений и желтизны',
                                      text="""<div class="content-text  muted777">

								
																<div class="introtext_wrapper">
			<div class="introtext">
									Появление желтизны на поверхности силиконовых чехлов обуславливается несколькими причинами. По факту, все упирается в естественный износ кейса. Аксессуары защищают смартфоны от механических повреждений. Но за долговечность самого материала отвечают другие факторы.							</div>
		</div>
														<p style="text-align: justify;">
 <b>Содержание:</b>
</p>
<ol>
	<li><a href="#pochemu-zhelteet-chekhol-iz-silikona" title="Почему желтеет чехол из силикона?">Почему желтеет чехол из силикона?</a></li>
	<li><a href="#kak-udalit-zheltiznu-s-chekhla" title="Как удалить желтизну с чехла?">Как удалить желтизну с чехла?</a>
	<ul>
		<li><a href="#metody-ochistki-prozrachnykh-chekhlov" title="Методы очистки прозрачных чехлов">Методы очистки прозрачных чехлов</a></li>
		<li><a href="#metody-promyvki-tsvetnykh-silikonovykh-chekhlov" title="Методы промывки цветных силиконовых чехлов">Методы промывки цветных силиконовых чехлов</a></li>
	</ul>
 </li>
	<li><a href="#kak-otbelit-silikonoviy-keys" title="Как отбелить силиконовый кейс?">Как отбелить силиконовый кейс?</a>
	<ul>
		<li><a href="#domashnie-sredstva" title="Домашние средства">Домашние средства</a></li>
		<li><a href="#professionalnye-sredstva" title="Профессиональные средства">Профессиональные средства</a></li>
	</ul>
 </li>
	<li><a href="#kak-izbezhat-poyavleniya-zheltizny" title="Как избежать появления желтизны?">Как избежать появления желтизны?</a></li>
</ol>
<p style="text-align: justify;">
	 Силиконовый чехол пользуется высоким спросом среди владельцев смартфонов по нескольким причинам. В первую очередь, это недорогой и надежный вариант защиты девайса. Его приятно держать в руках, а поверхность аксессуара оберегает устройство от падения. Также у прозрачных чехлов имеются и другие эксплуатационные преимущества: они предотвращают нагрев телефонов, попадание пыли и загрязнений, появление сколок и царапин.
</p>
<p style="text-align: justify;">
	 Несмотря на все достоинства силиконовых чехлов, у них есть и недостатки. Главный из них – появление желтизны на поверхности. В статье мы расскажем, из-за чего возникает данная проблема, и как очистить прозрачный кейс от загрязнений, не повредив при этом сам материал.
</p>
<h2 id="pochemu-zhelteet-chekhol-iz-silikona" style="text-align: justify;">
Почему желтеет чехол из силикона? </h2>
<p style="text-align: justify;">
	 Появление желтизны на поверхности силиконовых чехлов обуславливается несколькими причинами. По факту, все упирается в естественный износ кейса. Аксессуары защищают смартфоны от механических повреждений. Но за долговечность самого материала отвечают другие факторы.
</p>
<p style="text-align: justify;">
	 Первоначальный вид прозрачных силиконовых кейсов начинает портиться спустя несколько месяцев интенсивной эксплуатации. Появление желтых или темных пятен происходит по следующим причинам.
</p>
<ul>
	<li>Перегрев кейса. Из-за воздействий высоких температур силикон имеет свойство расширяться, в пористую структуру материала попадает пыль и грязь. Чаще всего это происходит, когда девайс долгое время находится под воздействием УФ лучей или отопительного оснащения. Желтые пятная на силиконовых аксессуарах могут возникать, если батарея телефона сильно нагревается во время зарядки. </li>
	<li>Отсутствие ухода. В повседневной жизни смартфон – наш неотъемлемый спутник. Мы берем его с собой на работу, в путешествия, спортзалы и т.д. Далеко не всегда поверхности, на которые кладется девайс, чистые. Кейс контактирует с пылью, грязью и иными веществами. Если не промыть аксессуар вовремя, на нем накопятся загрязнения, которые в будущем изменят цвет материала. </li>
	<li>Естественный износ. Даже при аккуратной эксплуатации чехол может желтеть. Происходят окислительные реакции кислорода и компонентов материала. Этого избежать нельзя. </li>
	<li>Табачный дым также впитывается в материал кейса и способствует образованию желтых пятен. </li>
</ul>
<p style="text-align: justify;">
	 Очистить силиконовый кейс и восстановить его внешний вид возможно. Чем быстрее это сделать, тем лучше будет результат.
</p>
<h2 id="kak-udalit-zheltiznu-s-chekhla" style="text-align: justify;">
Как удалить желтизну с чехла? </h2>
<p style="text-align: justify;">
	 На прозрачных моделях желтизна заметнее, чем на цветных аксессуарах. Но и почистить такой чехол легче, так как моющие средства не повредят его материал. Далее рассмотрим, какими методами можно убрать загрязнения с поверхности кейса.
</p>
<h3 id="metody-ochistki-prozrachnykh-chekhlov" style="text-align: justify;">
Методы очистки прозрачных чехлов </h3>
<p style="text-align: justify;">
	 Эффективнее всего проводить чистку пищевой содой. Схема действий простая:
</p>
<ol>
	<li>
	Промыть силиконовый кейс проточной водой, чтобы удалить загрязнения и другие вещества; </li>
	<li>
	Нанести пищевую соду на влажную поверхность кейса; </li>
	<li>
	Провести чистку силиконового аксессуара зубной щеткой. Лучше делать это деликатно, чтобы на поверхности не остались царапины; </li>
	<li>
	Промыть накладку водой и тщательно протереть. </li>
</ol>
<p style="text-align: justify;">
	 В некоторых случаях, когда загрязнения сильно въелись в материал, проводят повторную очистку аксессуара. Если сода не помогла, попробуйте более радикальный метод:
</p>
<ol>
	<li>
	Возьмите емкость и наполните ее водкой или спиртовым раствором; </li>
	<li>
	Поместите туда чехол примерно на 8-10 минут; </li>
	<li>
	Промойте и протрите кейс насухо. </li>
</ol>
<h3 id="metody-promyvki-tsvetnykh-silikonovykh-chekhlov" style="text-align: justify;">
Методы промывки цветных силиконовых чехлов </h3>
<p style="text-align: justify;">
	 Во время чистки цветных кейсов нельзя использовать средства, содержащие спирт, так как высока вероятность, что вы повредите слой краски. Также лучше отказаться от соды, для которой характерны абразивные свойства. Да, пятна уберутся, однако на поверхности могут образоваться царапины.
</p>
<p style="text-align: justify;">
	 Оптимальный вариант – провести очистку силиконового цветного чехла обычным хозяйственным мылом:
</p>
<ol>
	<li>
	Натрите кусок мыла на мелкой терке; </li>
	<li>
	Размешайте полученную стружку в теплой воде – она должна раствориться. Насыщенность раствора зависит от степени загрязнения чехла. </li>
	<li>
	Поместите в него кейс и оставьте на полтора часа; </li>
	<li>
	Промойте его под краном и аккуратно вытрите салфеткой или мягкой тканью. </li>
</ol>
<h2 id="kak-otbelit-silikonoviy-keys" style="text-align: justify;">
Как отбелить силиконовый кейс? </h2>
<p style="text-align: justify;">
	 Чтобы очистить кейс, можно использовать как домашние, так и профессиональные средства. С последними нужно быть аккуратнее, так как они могут навредить силикону. Важно правильно рассчитать дозу и время воздействия, чтобы пористая структура материала осталась неизменной.
</p>
<h3 id="domashnie-sredstva" style="text-align: justify;">
Домашние средства </h3>
<p style="text-align: justify;">
	 В случае небольших загрязнений можно попробовать средства, которые всегда под рукой: зубные пасты, перекись, мыльные растворы и т.д. Давайте разберем их более подробно.
</p>
<p style="text-align: justify;">
</p>
<ul>
	<li>Зубная паста</li>
</ul>
<p>
</p>
<p style="text-align: justify;">
	 Отбелить прозрачный кейс можно при помощи пасты. Нанесите ее на поверхность и смойте состав через 30 минут обычной водой. При необходимости можно повторить процедуру.
</p>
<p style="text-align: justify;">
</p>
<ul>
	<li>Перекись</li>
</ul>
<p>
</p>
<p style="text-align: justify;">
	 Перекисью можно не только отбелить силикон, но и продезинфицировать чехол. Раствор должен включать в себя 3% перекись и воду в пропорции 1:1. Поместите в него кейс на 15 минут, далее пройдитесь по аксессуару зубной щеткой и промойте под краном.
</p>
<p style="text-align: justify;">
</p>
<ul>
	<li>Бензин</li>
</ul>
<p>
</p>
<p style="text-align: justify;">
	 Его лучше использовать, когда остальные методы не принесли нужного результата. Вам понадобится бензин для зажигалок. Нанесите пару капель средства на ткань или ватный диск и протрите поверхность кейса. Чтобы избавиться от специфического запаха, промойте чехол со стиральным порошком.
</p>
<h3 id="professionalnye-sredstva" style="text-align: justify;">
Профессиональные средства </h3>
<p style="text-align: justify;">
	 Если домашние методы не помогли, попробуйте отмыть силиконовый аксессуар бытовой химией или средствами для стирки.
</p>
<p style="text-align: justify;">
</p>
<ul>
	<li>Жидкое мыло</li>
</ul>
<p>
</p>
<p style="text-align: justify;">
	 Средство поможет избавиться от желтых пятен, так как в его составе присутствует сульфанол. С его помощью растворяются органические соединения. Чтобы не навредить материалу, приготовьте раствор. Смешайте литр воды с чайной ложкой мыла, поместите туда аксессуар на полчаса, после чего промойте кейс губкой под краном.
</p>
<p style="text-align: justify;">
</p>
<ul>
	<li>Отбеливатель</li>
</ul>
<p>
</p>
<p style="text-align: justify;">
	 Почистить силиконовый кейс можно и отбеливателями. Смешайте моющее средство с теплой водой в соотношении 1:10. Нанесите его на губку или ватный диск и протрите аксессуар, чтобы удалить загрязнения.
</p>
<p style="text-align: justify;">
</p>
<ul>
	<li>Пятновыводитель</li>
</ul>
<p>
</p>
<p style="text-align: justify;">
	 Используйте средства, состав которых включает активный кислород и энзимы. Несмотря на то, что хлор более эффективен, он может навредить силиконовой поверхности чехла. Нанесите пятновыводитель на губку, протрите кейс и промойте его спустя 15 минут под водой.
</p>
<h2 id="kak-izbezhat-poyavleniya-zheltizny" style="text-align: justify;">
Как избежать появления желтизны? </h2>
<p style="text-align: justify;">
	 Чтобы прозрачный чехол не пожелтел раньше времени, соблюдайте несколько рекомендаций:
</p>
<ul>
	<li>Протирайте кейс влажной (желательно антибактериальной) салфеткой каждый день; </li>
	<li>Носите смартфон в отдельном кармане сумки, не допуская контакта с другими предметами; </li>
	<li>Следите за тем, куда кладете девайс. Грязных и липких поверхностей лучше избегать; </li>
	<li>Защищайте чехол от механических повреждений. Те же царапины легко забиваются грязью и ускоряют появление желтизны и темных пятен. </li>
</ul>
<p style="text-align: justify;">
	 Помните, что даже при аккуратной эксплуатации и тщательном уходе кейс со временем теряет свои внешние качества. Причина тому – естественный износ. Поэтому купить один чехол на «всю жизнь» смартфона не получится.
</p>			
			</div>""",
                                      image="images_aticle/2.webp",
                                      author=users[0],
                                      created_at='2024-02-26 09:49:40.227214+03',
                                      updated_at='2024-02-26 09:49:40.227214+03',
                                      date_published='2024-02-26 09:49:40.227214+03',
                                      published=True,
                                      number_of_views=42)
        Article.objects.get_or_create(
                                      title='Совместимость чехлов Samsung',
                                      text="""<div class="inner_wrapper_text">
			<div class="content-text  muted777">

								
																<div class="introtext_wrapper">
			<div class="introtext">
									<p style="text-align: justify;">
	 Смартфоны Samsung пользуются преимущественным спросом среди гаджетов на базе Android. Более того, компания является главным конкурентом Apple, и не сдает лидирующих позиций по сей день. Не удивительно, ведь смартфоны Самсунг представлены широкой линейкой, начиная с флагманских устройств, заканчивая бюджетными моделями. Любой желающий может подобрать телефон, опираясь на собственный бюджет и потребности.
</p>							</div>
		</div>
														<p style="text-align: justify;">
 <b>Содержание:</b>
</p>
<ul>
	<li><a href="#tablitsa-sravneniy-sovmestimosti-chekhlov-samsung" title="Таблица сравнений совместимости чехлов Samsung">Таблица сравнений совместимости чехлов Samsung</a>
	<ol>
	<li><a href="#seriya-smartfonov-samsung-galaxy-s" title="Серия смартфонов Samsung Galaxy S">Серия смартфонов Samsung Galaxy S</a></li>
	<li><a href="#seriya-smartfonov-samsung-galaxy-note" title="Серия смартфонов Samsung Galaxy Note">Серия смартфонов Samsung Galaxy Note</a></li>
	<li><a href="#seriya-smartfonov-samsung-galaxy-a" title="Серия смартфонов Samsung Galaxy A">Серия смартфонов Samsung Galaxy A</a></li>
	<li><a href="#seriya-smartfonov-samsung-galaxy-j" title="Серия смартфонов Samsung Galaxy J">Серия смартфонов Samsung Galaxy J</a></li>
	<li><a href="#seriya-smartfonov-samsung-galaxy-m" title="Серия смартфонов Samsung Galaxy M">Серия смартфонов Samsung Galaxy M</a></li>
</ol></li>
</ul>
<p style="text-align: justify;">
	 Спустя время каждый владелец задумывается о замене девайса на более совершенную модель. Если вы один из них, не спешите выкидывать старый чехол. Возможно, он идеально подойдет для нового устройства.
</p>
<p style="text-align: justify;">
	 В статье мы расскажем, какие чехлы разных моделей совместимы между собой.
</p>
<p style="text-align: justify;">
	 Обратите внимание: кейсы на смартфоны Xiaomi или Honor проще комбинировать с новыми телефонами линеек. Аксессуары на Samsung Galaxy или другие модели этой способностью обделены, за исключением нескольких девайсов.
</p>
<h2 id="tablitsa-sravneniy-sovmestimosti-chekhlov-samsung" style="text-align: justify;">В таблице сравнений мы покажем совместимость чехлов Samsung</h2>
<h3 id="seriya-smartfonov-samsung-galaxy-s" style="text-align: justify;">Серия смартфонов Samsung Galaxy S </h3>
<p style="text-align: justify;">
	 Телефоны Galaxy S3 и Galaxy S3 Neo подразумевают совместимость стекол и кейсов. В случае с другими устройствами линейки придется купить чехол под определенную модель.
</p>
<table style="width:100%" border="1" cellspacing="0" cellpadding="0">
<tbody>
<tr>
	<th style="text-align: center;">
			 Модель Samsung
	</th>
	<th style="text-align: center;">
			 Совместимость чехла
	</th>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S3
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Samsung Galaxy S3 Neo
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S3 Neo
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Samsung Galaxy S3
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S3 Mini
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S4
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S4 Mini
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S5 Mini
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S5
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S6 Edge
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S6 Edge +
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S7
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S7 Edge
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S8
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S8 Plus
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S9
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S9 Plus
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S10
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S10e
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S10 Plus
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S10 Lite
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S11
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S11e
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S11 Plus
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S20
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S20 Ultra
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S20 Plus
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S21
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S21 Ultra
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S21 +
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S22
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S22 Ultra
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy S22 +
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
</tbody>
</table>
<h3 id="seriya-smartfonov-samsung-galaxy-note" style="text-align: justify;">Серия смартфонов Samsung Galaxy Note </h3>
<p style="text-align: justify;">
	 К сожалению, смартфоны Galaxy Note отличаются между собой не только «начинкой», но и габаритами устройств. Поэтому вне зависимости от того, какой модели вы отдали предпочтение, придется приобретать соответствующий чехол или стекло.
</p>
<h3 id="seriya-smartfonov-samsung-galaxy-a" style="text-align: justify;">Серия смартфонов Samsung Galaxy A </h3>
<p style="text-align: justify;">
	 Защитные аксессуары комбинируются между собой у следующих моделей: Galaxy A8s и Galaxy A9 Pro, Galaxy A20 и Galaxy A30, Galaxy A50 и Galaxy A50s / A30s.
</p>
<table style="width:100%" border="1" cellspacing="0" cellpadding="0">
<tbody>
<tr>
	<th style="text-align: center;">
			 Модель Samsung
	</th>
	<th style="text-align: center;">
			 Совместимость чехла
	</th>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A3
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A5
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A7
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A3
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A5
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A7
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A3
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A5
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A7
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A6
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A6+
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A7
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A8
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A8+
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A9
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A8s
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy A9 Pro
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A2 Core
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A20e
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A10e
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A01
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A10
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A20
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy A30
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A30
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy A20
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A40
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A50
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy A50s / A30s
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A60
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A70
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 A80
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A90
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A10s
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A20s
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A30s
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy A50 / A50s
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A50s
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy A50 / A30s
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A11
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A21
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A31
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A41
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A51
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A52
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A53
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A71
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A72
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy A73
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
</tbody>
</table>
<h3 id="seriya-smartfonov-samsung-galaxy-j" style="text-align: justify;">Серия смартфонов Samsung Galaxy J </h3>
<p style="text-align: justify;">
	 Модели защитных стекол и чехлов на смартфоны Самсунг Галакси серии J тоже нельзя комбинировать между девайсами. Все дело в габаритах корпусов, которые отличаются в зависимости от устройства.
</p>
<h3 id="seriya-smartfonov-samsung-galaxy-m" style="text-align: justify;">Серия смартфонов Samsung Galaxy M </h3>
<p style="text-align: justify;">
	 В нескольких моделях телефонов линейки Galaxy M предусмотрена совместимость аксессуаров. К ним относят Galaxy M21 и Galaxy M30s.
</p>
<table style="width:100%" border="1" cellspacing="0" cellpadding="0">
<tbody>
<tr>
	<th style="text-align: center;">
			 Модель Samsung
	</th>
	<th style="text-align: center;">
			 Совместимость чехла
	</th>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M11
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M21
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy M30s
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M31
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M41
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M10
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M20
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M30s
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Galaxy M21
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M30
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
<tr>
	<td style="text-align: center;">
		<p>
			 Galaxy M40
		</p>
	</td>
	<td style="text-align: center;">
		<p>
			 Отсутствует
		</p>
	</td>
</tr>
</tbody>
</table>
<p style="text-align: justify;">
	<span style="color: var(--basic_text_black);">Таким образом, производитель телефонов Samsung не предусматривает совместимость чехлов и других защитных аксессуаров между новыми и старыми поколениями смартфонов. Особенно это касается моделей S20, S22, S21, A11, A53 и др.</span>
</p>
<p style="text-align: justify;">
	 Единственный выход – приобрести новый кейс именно под ваш смартфон. В нашем интернет-магазине представлены чехлы из различных материалов, таких как силикон, пластик или кожа. Все они отличаются между собой не только эксплуатационными параметрами, но и дизайном. Ознакомиться с ассортиментом можно в каталоге.
</p>			
			</div>
					</div>  """,
                                      image="images_aticle/3.png",
                                      author=users[0],
                                      created_at='2024-03-31 09:49:40+03',
                                      updated_at='2024-03-31 09:49:40.227214+03',
                                      date_published='2024-03-31 09:49:40.227214+03',
                                      published=True,
                                      number_of_views=27)
        print("blog-ok")
