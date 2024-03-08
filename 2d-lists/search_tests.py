from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    def test_search(self):
        #1
        expected_play_search_result = [
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]
            ]
        self.assertEqual(search('play'), expected_play_search_result)
        self.assertEqual(search('PLAY'), expected_play_search_result)
        self.assertEqual(search('pLaY'), expected_play_search_result)

        #2
        expected_empty_search_result = []
        self.assertEqual(search(''), expected_empty_search_result)

        #3
        expected_potato_search_result = []

        self.assertEqual(search('potato'), expected_potato_search_result)
        self.assertEqual(search('POTATO'), expected_potato_search_result)
        self.assertEqual(search('PoTaTo'), expected_potato_search_result)


    def test_article_length(self):
        #1
        expected_metadata_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        expected_article_length_soccer_2500_result = [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]

        self.assertEqual(article_length(1000, expected_metadata_soccer_results), [])
        self.assertEqual(article_length(2500, expected_metadata_soccer_results), expected_article_length_soccer_2500_result)
        self.assertEqual(article_length(6000, expected_metadata_soccer_results), expected_metadata_soccer_results)
        self.assertEqual(article_length(-7, expected_metadata_soccer_results), [])


        #2
        expected_play_metadata_results = [
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]
        ]
        expected_article_length_play_20000_result = [['Richard Wright (musician)', 'RussBot', 1189536295, 16185]]

        self.assertEqual(article_length(20000, expected_play_metadata_results), expected_article_length_play_20000_result)
        self.assertEqual(article_length(10000, expected_play_metadata_results), [])
        self.assertEqual(article_length(300000, expected_play_metadata_results), expected_play_metadata_results)
        self.assertEqual(article_length(-7000, expected_play_metadata_results), [])

        #3
        expected_potato_metadata_result = []
        self.assertEqual(article_length(10000, expected_potato_metadata_result), [])
        self.assertEqual(article_length(0, expected_potato_metadata_result), [])

        #4
        expected_empty_metadata_result = []
        self.assertEqual(article_length(10000, expected_empty_metadata_result), [])
        self.assertEqual(article_length(0, expected_empty_metadata_result), [])


    def test_unique_authors(self):
        #1
        expected_metadata_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        expected_unique_authors_3_results = [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]
        expected_unique_authors_20_results = [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]
        expected_unique_authors_0_results = []
        expected_unique_authors_negative_results = []

        self.assertEqual(unique_authors(3, expected_metadata_soccer_results), expected_unique_authors_3_results)
        self.assertEqual(unique_authors(20, expected_metadata_soccer_results), expected_unique_authors_20_results)
        self.assertEqual(unique_authors(0, expected_metadata_soccer_results), expected_unique_authors_0_results)
        self.assertEqual(unique_authors(-3, expected_metadata_soccer_results), expected_unique_authors_negative_results)

        #2
        expected_play_metadata_results = [
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]
        ]

        self.assertEqual(unique_authors(1, expected_play_metadata_results),[['Richard Wright (musician)', 'RussBot', 1189536295, 16185]])
        self.assertEqual(unique_authors(2, expected_play_metadata_results), expected_play_metadata_results)
        self.assertEqual(unique_authors(0, expected_play_metadata_results),[])
        self.assertEqual(unique_authors(-7, expected_play_metadata_results), [])

        #3
        expected_potato_metadata_result = []
        self.assertEqual(unique_authors(-7, expected_potato_metadata_result), [])
        self.assertEqual(unique_authors(0, expected_potato_metadata_result), [])
        self.assertEqual(unique_authors(10, expected_potato_metadata_result), [])

        #4
        expected_empty_metadata_result = []
        self.assertEqual(unique_authors(-7, expected_empty_metadata_result), [])
        self.assertEqual(unique_authors(0, expected_empty_metadata_result), [])
        self.assertEqual(unique_authors(10, expected_empty_metadata_result), [])


    def test_most_recent_article(self):
        #1
        expected_metadata_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(most_recent_article(expected_metadata_soccer_results), ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117])

        #2
        expected_play_metadata_results = [
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]
        ]
        self.assertEqual(most_recent_article(expected_play_metadata_results), ['Annie (musical)', 'Jack Johnson', 1223619626, 27558])

        #3
        expected_potato_metadata_result = []
        self.assertEqual(most_recent_article(expected_potato_metadata_result),"")

        #4
        expected_empty_metadata_result = []
        self.assertEqual(most_recent_article(expected_empty_metadata_result),"")

    
    def test_favorite_author(self):
        #1
        expected_metadata_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(favorite_author('Burna Boy', expected_metadata_soccer_results), True)
        self.assertEqual(favorite_author('burna boy', expected_metadata_soccer_results), True)
        self.assertEqual(favorite_author('BURNA BOY', expected_metadata_soccer_results), True)
        self.assertEqual(favorite_author('James Artur', expected_metadata_soccer_results), False)
        self.assertEqual(favorite_author('james artur', expected_metadata_soccer_results), False)
        self.assertEqual(favorite_author('JAMES ARTUR', expected_metadata_soccer_results), False)
        self.assertEqual(favorite_author('', expected_metadata_soccer_results), False)

        #2
        expected_play_metadata_results = [
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]
        ]
        self.assertEqual(favorite_author('Jack Johnson', expected_play_metadata_results), True)
        self.assertEqual(favorite_author('jack johnson', expected_play_metadata_results), True)
        self.assertEqual(favorite_author('JACK JOHNSON', expected_play_metadata_results), True)
        self.assertEqual(favorite_author('James Arthur', expected_play_metadata_results), False)
        self.assertEqual(favorite_author('JAMES ARTHUR', expected_play_metadata_results), False)
        self.assertEqual(favorite_author('james arthur', expected_play_metadata_results), False)
        self.assertEqual(favorite_author('', expected_play_metadata_results), False)

        #3
        expected_potato_metadata_results = []
        self.assertEqual(favorite_author('James Arthur', expected_potato_metadata_results), False)
        self.assertEqual(favorite_author('JAMES ARTHUR', expected_potato_metadata_results), False)
        self.assertEqual(favorite_author('james arthur', expected_potato_metadata_results), False)
        self.assertEqual(favorite_author('', expected_potato_metadata_results), False)
        
        #4
        expected_empty_metadata_results = []
        self.assertEqual(favorite_author('James Arthur', expected_empty_metadata_results), False)
        self.assertEqual(favorite_author('JAMES ARTHUR', expected_empty_metadata_results), False)
        self.assertEqual(favorite_author('james arthur', expected_empty_metadata_results), False)
        self.assertEqual(favorite_author('', expected_empty_metadata_results), False)


    def test_title_and_author(self):
        #1
        expected_metadata_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(title_and_author(expected_metadata_soccer_results), [('Spain national beach soccer team', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')])

        #2
        expected_play_metadata_results = [
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]
        ]
        self.assertEqual(title_and_author(expected_play_metadata_results),[('Richard Wright (musician)', 'RussBot'), ('Annie (musical)', 'Jack Johnson')])

        #3
        expected_potato_metadata_results = []
        self.assertEqual(title_and_author(expected_potato_metadata_results),[])

        #4
        expected_empty_metadata_results = []
        self.assertEqual(title_and_author(expected_empty_metadata_results),[])


    def test_refine_search(self):
        #1
        expected_metadata_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(refine_search('beach', expected_metadata_soccer_results),[['Spain national beach soccer team', 'jack johnson', 1233458894, 1526]])
        self.assertEqual(refine_search('apple', expected_metadata_soccer_results), [])
        self.assertEqual(refine_search('', expected_metadata_soccer_results), [])

        #2
        expected_play_metadata_results = [
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]
        ]
        self.assertEqual(refine_search('musical', expected_play_metadata_results),[['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Annie (musical)', 'Jack Johnson', 1223619626, 27558]])
        self.assertEqual(refine_search('apple', expected_play_metadata_results),[])
        self.assertEqual(refine_search('', expected_play_metadata_results),[])

        #3
        expected_potato_metadata_result = []
        self.assertEqual(refine_search('act', expected_potato_metadata_result),[])
        self.assertEqual(refine_search('', expected_potato_metadata_result),[])

        #4
        expected_empty_metadata_result = []
        self.assertEqual(refine_search('act', expected_empty_metadata_result),[])
        self.assertEqual(refine_search('', expected_empty_metadata_result),[])
    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_2(self, input_mock):
        #1
        keyword = 'soccer'
        advanced_option = 2
        advanced_response = 3

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"


        #2
        keyword = 'potato'
        advanced_option = 2
        advanced_response = 3

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"


    @patch('builtins.input')
    def test_advanced_option_3(self, input_mock):
        #1
        keyword = 'soccer'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nHere are your articles: ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]\n"

        #2
        keyword = 'potato'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nNo articles found\n"



    @patch('builtins.input')
    def test_advanced_option_4(self, input_mock):
        #1
        keyword = 'soccer'
        advanced_option = 4
        advanced_response_1 = 'burna boy'
        advanced_response_2 = 'james artur'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response_1])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response_1) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\nYour favorite author is in the returned articles!\n"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response_2])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response_2) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\nYour favorite author is not in the returned articles!\n"

        #2
        keyword = 'potato'
        advanced_option = 4
        advanced_response = 'james artur'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"


    @patch('builtins.input')
    def test_advanced_option_5(self, input_mock):
        #1
        keyword = 'soccer'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nHere are your articles: [('Spain national beach soccer team', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')]\n"


        #2
        keyword = 'potato'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nNo articles found\n"


    @patch('builtins.input')
    def test_advanced_option_6(self, input_mock):
        #1
        keyword = 'soccer'
        advanced_option = 6
        advanced_response_1 = 'beach'
        advanced_response_2 = 'apple'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response_1])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response_1) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526]]\n"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response_2])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response_2) + "\n\nNo articles found\n"

        #2
        keyword = 'potato'
        advanced_option = 6
        advanced_response = 'apple'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"



    @patch('builtins.input')
    def test_advanced_option_7(self, input_mock):
        #1
        keyword = 'soccer'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"


        #2
        keyword = 'potato'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nNo articles found\n"

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
