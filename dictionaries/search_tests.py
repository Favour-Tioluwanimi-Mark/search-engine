from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

#metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'and', 'rock', 'singer', 'songwriter', 'also', 'known', 'hip', 'hop', 'musician', 'folk', 'pop', 'composer', 'drummer', 'player', 'rapper', 'john', 'don', 'guitarist', 'the', 'andrew', 'country', 'indie', 'charlie', 'alternative', 'paul', 'bassist', 'cellist', 'pianist', 'artist']], ['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['List of overtone musicians', 'Mack Johnson', 1176928050, 2299, ['and', 'overtone', 'singing', 'the', 'with', 'from', 'musician', 'singer']]]
class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        metadata_1 = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'singer']], ['French pop music', 'Mack Johnson', 1172208041, 5569, ['artist', 'radio']], ['List of overtone musicians', 'Mack Johnson', 1176928050, 2299,['overtone', 'singer', 'musician']]]
        self.assertEqual(keyword_to_titles(metadata_1),{
            'canadian': ['List of Canadian musicians'],
            'singer': ['List of Canadian musicians', 'List of overtone musicians'],
            'radio': ['French pop music'],
            'artist': ['French pop music'],
            'overtone': ['List of overtone musicians'],
            'musician' : ['List of overtone musicians']
        })

        metadata_2 = [['Article_title1', 'author1', 558268, 2956,['keyword', 'keyword1', 'keyword2']], ['Article_title2', 'author2', 445578, 27483, ['keyword', 'keyword3']]]
        self.assertEqual(keyword_to_titles(metadata_2),{
            'keyword':['Article_title1', 'Article_title2'],
            'keyword1': ['Article_title1'],
            'keyword2': ['Article_title1'],
            'keyword3' : ['Article_title2']
        })

        metadata_3 = []
        self.assertEqual(keyword_to_titles(metadata_3),{})
    
    def test_title_to_info(self):
        metadata_1 = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'singer']], ['French pop music', 'Mack Johnson', 1172208041, 5569, ['artist', 'radio']], ['List of overtone musicians', 'Mack Johnson', 1176928050, 2299,['overtone', 'singer', 'musician']]]
        self.assertEqual(title_to_info(metadata_1),{
            'List of Canadian musicians': {'author':'Jack Johnson', 'timestamp': 1181623340, 'length': 21023},
            'French pop music': {'author':'Mack Johnson', 'timestamp': 1172208041, 'length': 5569},
            'List of overtone musicians': {'author':'Mack Johnson', 'timestamp': 1176928050, 'length': 2299}
        })
        metadata_2 = [['Article_title1', 'author1', 558268, 2956,['keyword', 'keyword1', 'keyword2']], ['Article_title2', 'author2', 445578, 27483, ['keyword', 'keyword3']]]
        self.assertEqual(title_to_info(metadata_2), {
            'Article_title1' : {'author': 'author1', 'timestamp': 558268, 'length': 2956},
            'Article_title2' : {'author': 'author2', 'timestamp': 445578, 'length': 27483}
        
        })
        metadata_3 = []
        self.assertEqual(title_to_info(metadata_3), {})

    def test_search(self):
        keyword_to_titles_metadata = {
            'canadian': ['List of Canadian musicians'],
            'singer': ['List of Canadian musicians', 'List of overtone musicians'],
            'radio': ['French pop music'],
            'artist': ['French pop music'],
            'overtone': ['List of overtone musicians'],
            'musician' : ['List of overtone musicians']
        }
        self.assertEqual(search('singer',keyword_to_titles_metadata), ['List of Canadian musicians', 'List of overtone musicians'])
        self.assertEqual(search('SINGER',keyword_to_titles_metadata), [])
        self.assertEqual(search('Singer',keyword_to_titles_metadata), [])
        self.assertEqual(search('',keyword_to_titles_metadata), []) 

    def test_article_length(self):
        article_titles_result = ['List of Canadian musicians', 'List of overtone musicians']
        title_to_info_result = {
            'List of Canadian musicians': {'author':'Jack Johnson', 'timestamp': 1181623340, 'length': 21023},
            'French pop music': {'author':'Mack Johnson', 'timestamp': 1172208041, 'length': 5569},
            'List of overtone musicians': {'author':'Mack Johnson', 'timestamp': 1176928050, 'length': 2299}
        }

        self.assertEqual(article_length(0, article_titles_result, title_to_info_result), [])
        self.assertEqual(article_length(500, article_titles_result, title_to_info_result), [])
        self.assertEqual(article_length(5000, article_titles_result, title_to_info_result), ['List of overtone musicians'])
        self.assertEqual(article_length(25000, article_titles_result, title_to_info_result), ['List of Canadian musicians', 'List of overtone musicians'])

    def test_key_by_author(self):
        title_to_info_result = {
            'List of Canadian musicians': {'author':'Jack Johnson', 'timestamp': 1181623340, 'length': 21023},
            'French pop music': {'author':'Mack Johnson', 'timestamp': 1172208041, 'length': 5569},
            'List of overtone musicians': {'author':'Mack Johnson', 'timestamp': 1176928050, 'length': 2299}
        }
        article_titles_result_1 = ['List of Canadian musicians', 'List of overtone musicians']
        self.assertEqual(key_by_author(article_titles_result_1, title_to_info_result), {
            'Jack Johnson': ['List of Canadian musicians'],
            'Mack Johnson': ['List of overtone musicians']
        })
        article_titles_result_2 = []
        self.assertEqual(key_by_author(article_titles_result_2, title_to_info_result), {})

        article_titles_result_3 = ['List of Canadian musicians', 'French pop music','List of overtone musicians']
        self.assertEqual(key_by_author(article_titles_result_3, title_to_info_result), {
            'Jack Johnson': ['List of Canadian musicians'],
            'Mack Johnson': ['French pop music', 'List of overtone musicians']
        })

    def test_filter_to_author(self):
        article_titles_result_2 = []
        article_titles_result = ['List of Canadian musicians', 'French pop music','List of overtone musicians']
        title_to_info_result = {
            'List of Canadian musicians': {'author':'Jack Johnson', 'timestamp': 1181623340, 'length': 21023},
            'French pop music': {'author':'Mack Johnson', 'timestamp': 1172208041, 'length': 5569},
            'List of overtone musicians': {'author':'Mack Johnson', 'timestamp': 1176928050, 'length': 2299}
        }
        self.assertEqual(filter_to_author('Mack Johnson', article_titles_result, title_to_info_result),['French pop music', 'List of overtone musicians'])
        self.assertEqual(filter_to_author('MACK JOHNSON', article_titles_result, title_to_info_result),[])
        self.assertEqual(filter_to_author('mack johnson', article_titles_result, title_to_info_result),[])
        self.assertEqual(filter_to_author('Jacob Wiliams', article_titles_result, title_to_info_result),[])
        self.assertEqual(filter_to_author('Mack Johnson', article_titles_result_2, title_to_info_result),[])
        self.assertEqual(filter_to_author('Jacob Williams', article_titles_result_2, title_to_info_result),[])



    def test_filter_out(self):
        article_titles_result = ['List of Canadian musicians', 'French pop music','List of overtone musicians']
        keyword_to_titles_result = {
                'canadian': ['List of Canadian musicians'],
                'singer': ['List of Canadian musicians', 'List of overtone musicians'],
                'radio': ['French pop music'],
                'artist': ['French pop music'],
                'overtone': ['List of overtone musicians'],
                'musician' : ['List of overtone musicians']
            }
        self.assertEqual(filter_out('radio', article_titles_result, keyword_to_titles_result),['List of Canadian musicians', 'List of overtone musicians'])
        self.assertEqual(filter_out('singer', article_titles_result, keyword_to_titles_result),['French pop music'])
        self.assertEqual(filter_out('place', article_titles_result, keyword_to_titles_result),['List of Canadian musicians', 'French pop music', 'List of overtone musicians'])
        self.assertEqual(filter_out('', article_titles_result, keyword_to_titles_result),['List of Canadian musicians', 'French pop music', 'List of overtone musicians'])



    def test_articles_from_year(self):
        article_titles_result = ['List of Canadian musicians', 'French pop music','List of overtone musicians']
        article_titles_result_2 = []
        title_to_info_result = {
            'List of Canadian musicians': {'author':'Jack Johnson', 'timestamp': 1181623340, 'length': 21023},
            'French pop music': {'author':'Mack Johnson', 'timestamp': 1172208041, 'length': 5569},
            'List of overtone musicians': {'author':'Mack Johnson', 'timestamp': 1176928050, 'length': 2299}
        }
        self.assertEqual(articles_from_year(2014, article_titles_result, title_to_info_result),[])
        self.assertEqual(articles_from_year(2007, article_titles_result, title_to_info_result),['List of Canadian musicians', 'French pop music','List of overtone musicians'])
        self.assertEqual(articles_from_year(2000, article_titles_result, title_to_info_result),[])
        self.assertEqual(articles_from_year(2014, article_titles_result_2, title_to_info_result),[])
        self.assertEqual(articles_from_year(2007, article_titles_result_2, title_to_info_result),[])
        self.assertEqual(articles_from_year(2000, article_titles_result_2, title_to_info_result),[])




    
    
       
        

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_1(self, input_mock):
        keyword = 'artist'
        advanced_option = 1
        advanced_response = 11000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['1986 in music']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_2(self, input_mock):
        keyword = 'cat'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Bearcat': ['Covariance and contravariance (computer science)']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_3(self, input_mock):
        keyword = 'singer'
        advanced_option = 3
        advanced_response = 'Mack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Rock music', 'List of overtone musicians', '1962 in country music']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_4(self, input_mock):
        keyword = 'singer'
        advanced_option = 4
        advanced_response = 'radio'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['1986 in music', '2009 in music', 'List of overtone musicians', 'Arabic music', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', '1996 in music', '2006 in music', 'Tony Kaye (musician)', '2007 in music', '2008 in music']\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_6(self, input_mock):
        keyword = 'singer'
        advanced_option = 6
        # advanced_response = ''

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of Canadian musicians', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'List of overtone musicians', 'Arabic music', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'Steve Perry (musician)', '1996 in music', '2006 in music', 'Tony Kaye (musician)', '2007 in music', '2008 in music']\n"

        self.assertEqual(output, expected)


# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
