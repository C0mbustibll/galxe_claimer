import aiohttp

class Gasless:

    @staticmethod
    async def check_tx_galxe(data):
        id = data['data']['prepareParticipate']['mintFuncInfo']['verifyIDs'][0]

        json_data = {
            'operationName': 'ParticipationInfo',
            'variables': {
                'ids': [
                    id,
                ],
            },
            'query': 'query ParticipationInfo($ids: [ID!]!) {\n  participations(id: $ids) {\n    id\n    tx\n    status\n    chain\n    __typename\n  }\n}\n',
        }

        async with aiohttp.ClientSession() as ses:
            async with ses.post('https://graphigo.prd.galaxy.eco/query', json=json_data) as res:
                return await res.json()


