# from src.utils.testing import E2ETest
# from src.common.models import Bank, Exchange
# from src.common.app import session, context
# from src.scrapers.popular.scraper import popular_scraper
#
#
# class TestBanreservasScraper(E2ETest):
#     def test_returns_correct_shape(self):
#         bank = Bank(id='popular', link='something')
#
#         with context():
#             session.add(bank)
#             session.commit()
#
#             banks = session.query(Bank).all()
#
#         self.assertEqual(len(banks), 1)
