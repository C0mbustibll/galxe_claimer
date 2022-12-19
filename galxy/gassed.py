import json
from web3 import Web3
from web3.eth import AsyncEth


class Gassed:

    def __init__(self, rpc):
        self.RPC = rpc

    contract_address = {
        '137': '0xf6D1B85af155229AcD7B523601148585A1ff67C6',
        '56': '0x2D18f2d27D50C9b4013DEBA3D54f60996bD8847E',
        '1': '0x75cdA57917E9F73705dc8BCF8A6B2f99AdBdc5a5',
        '43114': '0x13D8c4e3741e968Cc8E740bdB02537cB1d2d70e6',
        '42161': '0x9e6eF7F75ad88D4Edb4C9925C94B769C5b0d6281',
        '10': '0x2e42f214467f647Fe687Fd9a2bf3BAdDFA737465'
    }

    ABI = '[{"inputs":[{"internalType":"address","name":"_galaxy_signer","type":"address"},{"internalType":"address","name":"_campaign_setter","type":"address"},{"internalType":"address","name":"_contract_manager","type":"address"},{"internalType":"address","name":"_treasury_manager","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_cid","type":"uint256"}],"name":"EventActivateCampaign","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_cid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_dummyId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_nftID","type":"uint256"},{"indexed":false,"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"}],"name":"EventClaim","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_cid","type":"uint256"},{"indexed":false,"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"_nftIDArr","type":"uint256[]"},{"indexed":false,"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"}],"name":"EventClaimBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_cid","type":"uint256"},{"indexed":false,"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"_nftIDArr","type":"uint256[]"},{"indexed":false,"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_minted","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_cap","type":"uint256"}],"name":"EventClaimBatchCapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_cid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_dummyId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_nftID","type":"uint256"},{"indexed":false,"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_minted","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_cap","type":"uint256"}],"name":"EventClaimCapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_cid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_dummyId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_nftID","type":"uint256"},{"indexed":false,"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"indexed":false,"internalType":"address","name":"_sender","type":"address"}],"name":"EventForge","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"address","name":"_account","type":"address"}],"name":"_hash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"internalType":"uint256[]","name":"_powahArr","type":"uint256[]"},{"internalType":"address","name":"_account","type":"address"}],"name":"_hashBatch","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"internalType":"uint256[]","name":"_powahArr","type":"uint256[]"},{"internalType":"uint256","name":"_cap","type":"uint256"},{"internalType":"address","name":"_account","type":"address"}],"name":"_hashBatchCapped","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"uint256","name":"_cap","type":"uint256"},{"internalType":"address","name":"_account","type":"address"}],"name":"_hashCapped","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_nftIDs","type":"uint256[]"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"address","name":"_account","type":"address"}],"name":"_hashForge","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"_verify","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"uint256","name":"_platformFee","type":"uint256"},{"internalType":"uint256","name":"_erc20Fee","type":"uint256"},{"internalType":"address","name":"_erc20","type":"address"}],"name":"activateCampaign","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"campaignFeeConfigs","outputs":[{"internalType":"address","name":"erc20","type":"address"},{"internalType":"uint256","name":"erc20Fee","type":"uint256"},{"internalType":"uint256","name":"platformFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"campaign_setter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"address","name":"_mintTo","type":"address"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"internalType":"uint256[]","name":"_powahArr","type":"uint256[]"},{"internalType":"address","name":"_mintTo","type":"address"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claimBatch","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"internalType":"uint256[]","name":"_powahArr","type":"uint256[]"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claimBatch","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"internalType":"uint256[]","name":"_powahArr","type":"uint256[]"},{"internalType":"uint256","name":"_cap","type":"uint256"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claimBatchCapped","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_dummyIdArr","type":"uint256[]"},{"internalType":"uint256[]","name":"_powahArr","type":"uint256[]"},{"internalType":"uint256","name":"_cap","type":"uint256"},{"internalType":"address","name":"_mintTo","type":"address"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claimBatchCapped","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"uint256","name":"_cap","type":"uint256"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claimCapped","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"uint256","name":"_cap","type":"uint256"},{"internalType":"address","name":"_mintTo","type":"address"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"claimCapped","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_nftIDs","type":"uint256[]"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"forge","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_cid","type":"uint256"},{"internalType":"contract IStarNFT","name":"_starNFT","type":"address"},{"internalType":"uint256[]","name":"_nftIDs","type":"uint256[]"},{"internalType":"uint256","name":"_dummyId","type":"uint256"},{"internalType":"uint256","name":"_powah","type":"uint256"},{"internalType":"address","name":"_mintTo","type":"address"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"forge","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"galaxy_signer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"hasMinted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"numMinted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_paused","type":"bool"}],"name":"setPause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"treasury_manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newAddress","type":"address"}],"name":"updateCampaignSetter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newAddress","type":"address"}],"name":"updateGalaxySigner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newAddress","type":"address"}],"name":"updateManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"newAddress","type":"address"}],"name":"updateTreasureManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

    async def mint(self,key, numb_id, address_nft, powahs, id_claim, _signature):
        web3 =Web3(Web3.AsyncHTTPProvider(self.RPC),
            modules={'eth': (AsyncEth,)}, middlewares=[])

        contract = web3.eth.contract(abi=json.loads(self.ABI))
        data = contract.encodeABI('claim',
                           args=[numb_id, web3.toChecksumAddress(address_nft), id_claim, powahs, web3.toBytes(hexstr=_signature)])

        ADDRESS = web3.eth.account.from_key(key).address

        tx = {
            'nonce': await web3.eth.get_transaction_count(ADDRESS),
            'gasPrice': await web3.eth.gas_price,
            'chainId': await web3.eth.chain_id,
            'from': ADDRESS,
            'to': web3.toChecksumAddress(self.contract_address[str(await web3.eth.chain_id)]),
            'data': data
        }
        tx['gas'] = int(await web3.eth.estimate_gas(tx) * 1.25)

        sign = web3.eth.account.sign_transaction(tx, key)
        hash = await web3.eth.send_raw_transaction(sign.rawTransaction)
        return hash

    async def verif_tx(self,tx_hash):
        web3 = Web3(Web3.AsyncHTTPProvider(self.RPC),
                    modules={'eth': (AsyncEth,)}, middlewares=[])
        try:
            data = await web3.eth.wait_for_transaction_receipt(tx_hash, timeout=200)
            if data.get('status') != None and data.get('status') == 1:
                return True
            else:
                return False
        except Exception as e:
            return False





