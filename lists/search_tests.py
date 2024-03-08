from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)

    def test_search(self):
        # 1
        expected_tion_search_result = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        self.assertEqual(search('tion'), expected_tion_search_result)
        self.assertEqual(search('TION'), expected_tion_search_result)
        self.assertEqual(search('TiOn'), expected_tion_search_result)

        # 2
        expected_plate_search_result = []
        self.assertEqual(search('plate'), expected_plate_search_result)
        self.assertEqual(search('PLATE'), expected_plate_search_result)
        self.assertEqual(search('PlAtE'), expected_plate_search_result)

        # 3
        expected_cat_search_result = ['Voice classification in non-classical music']
        self.assertEqual(search('cat'), expected_cat_search_result)
        self.assertEqual(search('CAT'), expected_cat_search_result)
        self.assertEqual(search('cAt'), expected_cat_search_result)

        # 4
        expected_empty_string_search_result = []
        self.assertEqual(search(''), expected_empty_string_search_result)

    def test_title_length(self):
        # 1
        dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        expected_dog_title_length_50_result = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        expected_dog_title_length_15_result = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Dalmatian (dog)', 'Guide dog', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']
        expected_dog_title_length_7_result =  ['Sun dog']
        expected_dog_title_length_2_result = []
        expected_dog_title_length_0_result = []

        self.assertEqual(title_length(50,dog_search_results),expected_dog_title_length_50_result)
        self.assertEqual(title_length(15,dog_search_results),expected_dog_title_length_15_result)
        self.assertEqual(title_length(7,dog_search_results),expected_dog_title_length_7_result)
        self.assertEqual(title_length(2,dog_search_results),expected_dog_title_length_2_result)
        self.assertEqual(title_length(0,dog_search_results),expected_dog_title_length_0_result)

        # 2
        tion_search_results = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        expected_tion_title_length_50_result = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', 'China national soccer team', 'Traditional Thai musical instruments']
        expected_tion_title_length_15_result = []
        expected_tion_title_length_7_result = []
        expected_tion_title_length_2_result = []
        expected_tion_title_length_0_result = []

        self.assertEqual(title_length(50,tion_search_results),expected_tion_title_length_50_result)
        self.assertEqual(title_length(15,tion_search_results),expected_tion_title_length_15_result)
        self.assertEqual(title_length(7,tion_search_results),expected_tion_title_length_7_result)
        self.assertEqual(title_length(2,tion_search_results),expected_tion_title_length_2_result)
        self.assertEqual(title_length(0,tion_search_results),expected_tion_title_length_0_result)

        # 3
        plate_search_results = []
        expected_plate_title_length_50_result = []
        expected_plate_title_length_15_result = []
        expected_plate_title_length_7_result = []
        expected_plate_title_length_2_result = []
        expected_plate_title_length_0_result = []

        self.assertEqual(title_length(50,plate_search_results),expected_plate_title_length_50_result)
        self.assertEqual(title_length(15,plate_search_results),expected_plate_title_length_15_result)
        self.assertEqual(title_length(7,plate_search_results),expected_plate_title_length_7_result)
        self.assertEqual(title_length(2,plate_search_results),expected_plate_title_length_2_result)
        self.assertEqual(title_length(0,plate_search_results),expected_plate_title_length_0_result)

        # 4
        cat_search_results = ['Voice classification in non-classical music']
        expected_cat_title_length_50_result = ['Voice classification in non-classical music']
        expected_cat_title_length_15_result = []
        expected_cat_title_length_7_result = []
        expected_cat_title_length_2_result = []
        expected_cat_title_length_0_result = []

        self.assertEqual(title_length(50,cat_search_results),expected_cat_title_length_50_result)
        self.assertEqual(title_length(15,cat_search_results),expected_cat_title_length_15_result)
        self.assertEqual(title_length(7,cat_search_results),expected_cat_title_length_7_result)
        self.assertEqual(title_length(2,cat_search_results),expected_cat_title_length_2_result)
        self.assertEqual(title_length(0,cat_search_results),expected_cat_title_length_0_result)


    def test_article_count(self):
        # 1
        dog_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        expected_dog_article_count_50_result = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        expected_dog_article_count_10_result = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football']
        expected_dog_article_count_5_result = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season']
        expected_dog_article_count_0_result = []

        self.assertEqual(article_count(50,dog_titles),expected_dog_article_count_50_result)
        self.assertEqual(article_count(10,dog_titles),expected_dog_article_count_10_result)
        self.assertEqual(article_count(5,dog_titles),expected_dog_article_count_5_result)
        self.assertEqual(article_count(0,dog_titles),expected_dog_article_count_0_result)

        # 2
        tion_titles = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        expected_tion_article_count_50_result = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        expected_tion_article_count_10_result = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        expected_tion_article_count_5_result = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team']
        expected_tion_article_count_0_result = []

        self.assertEqual(article_count(50,tion_titles),expected_tion_article_count_50_result)
        self.assertEqual(article_count(10,tion_titles),expected_tion_article_count_10_result)
        self.assertEqual(article_count(5,tion_titles),expected_tion_article_count_5_result)
        self.assertEqual(article_count(0,tion_titles),expected_tion_article_count_0_result)

        # 3
        plate_titles = []
        expected_plate_article_count_result = []

        self.assertEqual(article_count(50,plate_titles),expected_plate_article_count_result)
        self.assertEqual(article_count(10,plate_titles),expected_plate_article_count_result)
        self.assertEqual(article_count(5,plate_titles),expected_plate_article_count_result)
        self.assertEqual(article_count(0,plate_titles),expected_plate_article_count_result)

        # 4
        cat_titles = ['Voice classification in non-classical music']
        expected_cat_article_count_50_result = ['Voice classification in non-classical music']
        expected_cat_article_count_10_result = ['Voice classification in non-classical music']
        expected_cat_article_count_5_result = ['Voice classification in non-classical music']
        expected_cat_article_count_0_result = []

        self.assertEqual(article_count(50,cat_titles),expected_cat_article_count_50_result)
        self.assertEqual(article_count(10,cat_titles),expected_cat_article_count_10_result)
        self.assertEqual(article_count(5,cat_titles),expected_cat_article_count_5_result)
        self.assertEqual(article_count(0,cat_titles),expected_cat_article_count_0_result)


    def test_random_article(self):
        # 1
        dog_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(random_article(5,dog_titles),'Mexican dog-faced bat')
        self.assertEqual(random_article(10,dog_titles),'Endoglin')
        self.assertEqual(random_article(-1,dog_titles),'')
        self.assertEqual(random_article(50,dog_titles),'')

        # 2
        tion_titles = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        self.assertEqual(random_article(4,tion_titles),'China national soccer team')
        self.assertEqual(random_article(6,tion_titles),'Comparison of programming languages (basic instructions)')
        self.assertEqual(random_article(-5,tion_titles),'')
        self.assertEqual(random_article(20,tion_titles),'')

        # 3
        plate_titles = []
        self.assertEqual(random_article(4,plate_titles),'')
        self.assertEqual(random_article(6,plate_titles),'')
        self.assertEqual(random_article(-5,plate_titles),'')
        self.assertEqual(random_article(20,plate_titles),'')

        # 4
        cat_titles = ['Voice classification in non-classical music']
        self.assertEqual(random_article(4,cat_titles),'')
        self.assertEqual(random_article(0,cat_titles),'Voice classification in non-classical music')
        self.assertEqual(random_article(-5,cat_titles),'')



    def test_favorite_article(self):
        # 1
        dog_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(favorite_article('endogenous cannabinoid',dog_titles),True)
        self.assertEqual(favorite_article('KeViN CaDoGaN',dog_titles),True)
        self.assertEqual(favorite_article('BLACK DOG (GHOST)',dog_titles),True)
        self.assertEqual(favorite_article('',dog_titles),False)
        self.assertEqual(favorite_article('Adam Keller',dog_titles),False)

        # 2
        tion_titles = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        self.assertEqual(favorite_article('comparison of programming languages (basic instructions)',tion_titles),True)
        self.assertEqual(favorite_article('CHINA NATIONAL SOCCER TEAM',tion_titles),True)
        self.assertEqual(favorite_article('Traditional THAI musical INSTRUMENTS',tion_titles),True)
        self.assertEqual(favorite_article('',tion_titles),False)
        self.assertEqual(favorite_article('Adam Keller',tion_titles),False)

        # 3
        plate_titles = []
        self.assertEqual(favorite_article('',plate_titles),False)
        self.assertEqual(favorite_article('Adam Keller',plate_titles),False)

        # 4
        cat_titles = ['Voice classification in non-classical music']
        self.assertEqual(favorite_article('voice classification in non-classical music',cat_titles),True)
        self.assertEqual(favorite_article('VOICE classification IN non-classical MUSIC',cat_titles),True)
        self.assertEqual(favorite_article('VOICE CLASSIFICATION IN NON-CLASSICAL MUSIC',cat_titles),True)
        self.assertEqual(favorite_article('',cat_titles),False)
        self.assertEqual(favorite_article('Adam Keller',cat_titles),False)


    def test_multiple_keywords(self):
        # 1 dog and cat
        dog_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        cat_titles = ['Voice classification in non-classical music']
        dog_cat_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Voice classification in non-classical music']
        self.assertEqual(multiple_keywords('cat',dog_titles.copy()),dog_cat_titles)
        self.assertEqual(multiple_keywords('CAT',dog_titles.copy()),dog_cat_titles)
        self.assertEqual(multiple_keywords('CaT',dog_titles.copy()),dog_cat_titles)

        # 2 dog and tion
        dog_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        tion_titles = ['Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        dog_tion_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Spain national beach soccer team', 'Reflection-oriented programming', 'Voice classification in non-classical music', "United States men's national soccer team 2009 results", 'China national soccer team', 'Traditional Thai musical instruments', 'Comparison of programming languages (basic instructions)']
        self.assertEqual(multiple_keywords('tion',dog_titles.copy()),dog_tion_titles)
        self.assertEqual(multiple_keywords('TION',dog_titles.copy()),dog_tion_titles)
        self.assertEqual(multiple_keywords('TiOn',dog_titles.copy()),dog_tion_titles)

        # 3 dog and plate
        dog_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        plate_titles = []
        dog_plate_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(multiple_keywords('plate',dog_titles.copy()),dog_plate_titles)
        self.assertEqual(multiple_keywords('PLATE',dog_titles.copy()),dog_plate_titles)
        self.assertEqual(multiple_keywords('PlAtE',dog_titles.copy()),dog_plate_titles)

        # 4 dog and empty string
        dog_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        empty_string = []
        dog_empty_titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(multiple_keywords('',dog_titles),dog_empty_titles)
        




    
        

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_1(self,input_mock):
        # 1
        keyword = 'dog'
        advanced_option = 1
        title_length = 15
        output = get_print(input_mock, [keyword, advanced_option, title_length])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(title_length) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Dalmatian (dog)', 'Guide dog', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']\n"
        self.assertEqual(output, expected)

        # 2
        keyword = 'plate'
        advanced_option = 1
        title_length = 15
        output = get_print(input_mock, [keyword, advanced_option, title_length])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(title_length) + "\n\nNo articles found\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_2(self,input_mock):
        # 1
        keyword = 'dog'
        advanced_option = 2
        article_count = 7
        output = get_print(input_mock, [keyword, advanced_option, article_count])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(article_count) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)']\n"
        self.assertEqual(output, expected)

        # 2
        keyword = 'plate'
        advanced_option = 2
        article_count = 7
        output = get_print(input_mock, [keyword, advanced_option, article_count])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(article_count) + "\n\nNo articles found\n"
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_3(self,input_mock):
        # 1
        keyword = 'dog'
        advanced_option = 3
        index = 7
        output = get_print(input_mock, [keyword, advanced_option, index])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(index) + "\n\nHere are your articles: Guide dog\n"
        self.assertEqual(output, expected)

        # 2
        keyword = 'plate'
        advanced_option = 3
        index = 7
        output = get_print(input_mock, [keyword, advanced_option, index])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(index) + "\n\nNo articles found\n"
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_4(self,input_mock):
        # 1
        keyword = 'dog'
        advanced_option = 4
        favorite_article = 'Kevin Cadogan'
        output = get_print(input_mock, [keyword, advanced_option, favorite_article])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(favorite_article) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\nYour favorite article is in the returned articles!\n"
        self.assertEqual(output, expected)

        keyword = 'dog'
        advanced_option = 4
        favorite_article = 'Adam Keller'
        output = get_print(input_mock, [keyword, advanced_option, favorite_article])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(favorite_article) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\nYour favorite article is not in the returned articles!\n"
        self.assertEqual(output, expected)

        # 2
        keyword = 'plate'
        advanced_option = 4
        favorite_article = 'Adam Keller'
        output = get_print(input_mock, [keyword, advanced_option, favorite_article])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(favorite_article) + "\n\nNo articles found\nYour favorite article is not in the returned articles!\n"
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_5(self,input_mock):
        # 1
        keyword = 'dog'
        advanced_option = 5
        other_keyword = 'cat'
        output = get_print(input_mock, [keyword, advanced_option, other_keyword])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(other_keyword) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Voice classification in non-classical music']\n"
        self.assertEqual(output, expected)

        # 2
        keyword = 'dog'
        advanced_option = 5
        other_keyword = 'plate'
        output = get_print(input_mock, [keyword, advanced_option, other_keyword])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(other_keyword) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_6(self,input_mock):
        # 1
        keyword = 'cat'
        advanced_option = 6
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Voice classification in non-classical music']\n"
        self.assertEqual(output, expected)

        # 2
        keyword = 'plate'
        advanced_option = 6
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"
        self.assertEqual(output, expected)

    




# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
