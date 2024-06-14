from random import choice

from config import ACCOUNTS, FEATURES
from hamster_client import BOOST_ENERGY, HamsterClient, sleep, logging
from strings import DELIMITER

clients = [HamsterClient(**options) for options in ACCOUNTS]


def main():
    while True:
        for client in clients:
            print(DELIMITER)
            client.sync()
            client.claim_daily_cipher()
            client.tap()
            client.buy_upgrades()
            client.check_task()
            client.claim_combo_reward()
            if client.is_taps_boost_available:
                client.boost(BOOST_ENERGY)
            logging.info(client.log_prefix + " ".join(f"{k}: {v} |" for k, v in client.stats.items()))
            print(DELIMITER)
            sleep(choice(range(1, 10)))
        sleep(FEATURES.get('delay_between_attempts', 60 * 1))


if __name__ == "__main__":
    main()
