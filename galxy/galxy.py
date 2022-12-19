from requests_html import AsyncHTMLSession
from uuid import uuid4
import time
import json
import aiohttp
from loguru import logger

class Galxy:

    @staticmethod
    async def claim(address: str, campaign_id: str, W: str,
                    CHAIN_CAMP: str = 'MATIC'):  # type: (str, str, str, str) -> Coroutine
        session = AsyncHTMLSession()

        call = int(time.time() * 1e3)
        params = {
            'captcha_id': '244bcb8b9846215df5af4c624a750db4',
            'challenge': uuid4(),
            'client_type': 'web',
            'lang': 'et',
            'callback': 'geetest_{}'.format(call),
        }

        resp = await session.get('https://gcaptcha4.geetest.com/load', params=params)
        js_data = json.loads(resp.text.strip('geetest_{}('.format(call)).strip(')'))['data']

        params = {
            'captcha_id': '244bcb8b9846215df5af4c624a750db4',
            'client_type': 'web',
            'lot_number': js_data['lot_number'],
            'payload': js_data['payload'],
            'process_token': js_data['process_token'],
            'payload_protocol': '1',
            'pt': '1',
            'w': W,
            'callback': 'geetest_{}'.format(call),
        }

        resp_complete = await session.get('https://gcaptcha4.geetest.com/verify', params=params)
        COMPLETED_DATA = json.loads(resp_complete.text.strip('geetest_{}('.format(call)).strip(')'))['data']

        json_data = {
            'operationName': 'PrepareParticipate',
            'variables': {
                'input': {
                    'signature': '',
                    'campaignID': campaign_id,
                    'address': address,
                    'mintCount': 1,
                    'chain': CHAIN_CAMP,
                    'captcha': {
                        'lotNumber': COMPLETED_DATA['lot_number'],
                        'captchaOutput': COMPLETED_DATA['seccode']['captcha_output'],
                        'passToken': COMPLETED_DATA['seccode']['pass_token'],
                        'genTime': COMPLETED_DATA['seccode']['gen_time'],
                    },
                },
            },
            'query': 'mutation PrepareParticipate($input: PrepareParticipateInput!) {\n  prepareParticipate(input: $input) {\n    allow\n    disallowReason\n    signature\n    nonce\n    mintFuncInfo {\n      funcName\n      nftCoreAddress\n      verifyIDs\n      powahs\n      cap\n      __typename\n    }\n    extLinkResp {\n      success\n      data\n      error\n      __typename\n    }\n    metaTxResp {\n      metaSig2\n      autoTaskUrl\n      metaSpaceAddr\n      forwarderAddr\n      metaTxHash\n      reqQueueing\n      __typename\n    }\n    solanaTxResp {\n      mint\n      updateAuthority\n      explorerUrl\n      signedTx\n      verifyID\n      __typename\n    }\n    aptosTxResp {\n      signatureExpiredAt\n      tokenName\n      __typename\n    }\n    __typename\n  }\n}\n',
        }
        headers = {
            'authority': 'graphigo.prd.galaxy.eco',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.103 Safari/537.36',
            'content-type': 'application/json',
        }
        async with aiohttp.ClientSession() as ses:
            async with ses.post('https://graphigo.prd.galaxy.eco/query', headers=headers,
                                data=json.dumps(json_data)) as r:
                data = await r.json()
                return data

    @staticmethod
    async def get_info_by_id(id):
        HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36',
        }

        json_data = {
            'operationName': 'CampaignInfo',
            'variables': {
                'address': '',
                'id': id,
            },
            'query': 'query CampaignInfo($id: ID!, $address: String!) {\n  campaign(id: $id) {\n    ...CampaignDetailFrag\n    space {\n      ...SpaceDetail\n      isAdmin(address: $address)\n      __typename\n    }\n    isBookmarked(address: $address)\n    childrenCampaigns {\n      ...CampaignDetailFrag\n      parentCampaign {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CampaignDetailFrag on Campaign {\n  id\n  ...CampaignMedia\n  name\n  numberID\n  type\n  cap\n  info\n  useCred\n  formula\n  status\n  creator\n  numNFTMinted\n  thumbnail\n  gasType\n  isPrivate\n  createdAt\n  requirementInfo\n  description\n  enableWhitelist\n  chain\n  startTime\n  endTime\n  requireEmail\n  requireUsername\n  blacklistCountryCodes\n  whitelistRegions\n  participants {\n    participantsCount\n    bountyWinnersCount\n    __typename\n  }\n  rewardType\n  distributionType\n  rewardName\n  spaceStation {\n    id\n    address\n    chain\n    __typename\n  }\n  ...WhitelistInfoFrag\n  ...WhitelistSubgraphFrag\n  gamification {\n    ...GamificationDetailFrag\n    __typename\n  }\n  creds {\n    ...CredForAddress\n    __typename\n  }\n  dao {\n    ...DaoSnap\n    nftCores {\n      list {\n        capable\n        marketLink\n        contractAddress\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DaoSnap on DAO {\n  id\n  name\n  logo\n  alias\n  isVerified\n  __typename\n}\n\nfragment CampaignMedia on Campaign {\n  thumbnail\n  rewardName\n  type\n  gamification {\n    id\n    type\n    __typename\n  }\n  __typename\n}\n\nfragment CredForAddress on Cred {\n  id\n  name\n  type\n  credType\n  credSource\n  referenceLink\n  description\n  lastUpdate\n  credContractNFTHolder {\n    timestamp\n    __typename\n  }\n  chain\n  eligible(address: $address)\n  subgraph {\n    endpoint\n    query\n    expression\n    __typename\n  }\n  __typename\n}\n\nfragment WhitelistInfoFrag on Campaign {\n  id\n  whitelistInfo(address: $address) {\n    address\n    maxCount\n    usedCount\n    __typename\n  }\n  __typename\n}\n\nfragment WhitelistSubgraphFrag on Campaign {\n  id\n  whitelistSubgraph {\n    query\n    endpoint\n    expression\n    variable\n    __typename\n  }\n  __typename\n}\n\nfragment GamificationDetailFrag on Gamification {\n  id\n  type\n  nfts {\n    nft {\n      id\n      animationURL\n      category\n      powah\n      image\n      name\n      treasureBack\n      nftCore {\n        ...NftCoreInfoFrag\n        __typename\n      }\n      traits {\n        name\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  airdrop {\n    name\n    contractAddress\n    token {\n      address\n      icon\n      symbol\n      __typename\n    }\n    merkleTreeUrl\n    addressInfo(address: $address) {\n      index\n      amount {\n        amount\n        ether\n        __typename\n      }\n      proofs\n      __typename\n    }\n    __typename\n  }\n  forgeConfig {\n    minNFTCount\n    maxNFTCount\n    requiredNFTs {\n      nft {\n        category\n        powah\n        image\n        name\n        nftCore {\n          capable\n          contractAddress\n          __typename\n        }\n        __typename\n      }\n      count\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment NftCoreInfoFrag on NFTCore {\n  id\n  capable\n  chain\n  contractAddress\n  name\n  symbol\n  dao {\n    id\n    name\n    logo\n    alias\n    __typename\n  }\n  __typename\n}\n\nfragment SpaceDetail on Space {\n  id\n  name\n  info\n  thumbnail\n  alias\n  links\n  isVerified\n  __typename\n}\n',
        }
        async with aiohttp.ClientSession() as session:
            async with session.post('https://graphigo.prd.galaxy.eco/query', headers=HEADERS,
                                    json=json_data) as response:
                return await response.json()

    @classmethod
    async def __validation_captcha(cls,CAPTCHA_W):
        session = AsyncHTMLSession()

        call = int(time.time() * 1e3)
        params = {
            'captcha_id': '244bcb8b9846215df5af4c624a750db4',
            'challenge': uuid4(),
            'client_type': 'web',
            'lang': 'et',
            'callback': 'geetest_{}'.format(call),
        }

        resp = await session.get('https://gcaptcha4.geetest.com/load', params=params)
        js_data = json.loads(resp.text.strip('geetest_{}('.format(call)).strip(')'))['data']

        params = {
            'captcha_id': '244bcb8b9846215df5af4c624a750db4',
            'client_type': 'web',
            'lot_number': js_data['lot_number'],
            'payload': js_data['payload'],
            'process_token': js_data['process_token'],
            'payload_protocol': '1',
            'pt': '1',
            'w': CAPTCHA_W,
            'callback': 'geetest_{}'.format(call),
        }

        resp_complete = await session.get('https://gcaptcha4.geetest.com/verify', params=params)
        VALIDATION = json.loads((resp_complete.text).strip('geetest_{}('.format(call)).strip(')'))['status']
        return VALIDATION


    @classmethod
    async def validation_config_w(cls, CAPTCHA_W):
        try:
            data = await cls.__validation_captcha(CAPTCHA_W)
            if data == 'success':
                logger.success('VALIDATION CAPTCHA | SUCCESS')
                return True

            if data == 'error':
                logger.error('VALIDATION CAPTCHA | FALSE ')
                return False

            logger.error('VALIDATION CAPTCHA | FALSE | UNKNOWN PARAMETERS | {}'.format(data))
            return False
        except Exception as e:
            logger.error('VALIDATION CAPTCHA ERROR | FALSE | {}'.format(e))
            return False