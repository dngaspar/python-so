import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "cookie": "_gcl_au=1.1.805920806.1678852014; keen={%22uuid%22:%2233492adb-d2d1-4a90-83ce-56c69b6cf5c0%22%2C%22initialReferrer%22:%22https://crowdworks.jp/%22}; _im_id.1008949=6ec0540992ea08e3.1678852019.; watchlist_session_id=8e95c3e5c8a84ee683b19f0d0e7705aabc3fe99dbcbb1c3171e95ec52ec5862e24c2e78ed73182d0; __lt__cid=19bb268b-b7bd-425b-a42a-eb32a9862b2e; _rt.uid=5331054; landing_url=https%3A%2F%2Fcrowdworks.jp%2F; count_of_member_merit_modal_show=3; _uetvid=14cc7b00c3ea11edaa733b857bf2158f; referer_url=https%3A%2F%2Fwww.google.com%2F; _ga=GA1.1.1071140694.1678852014; logged_in=true; _cw_session_id=3d2fefa2e8983bcf269b26f14ddfa5c6; _ga_WC7RFDVS0V=GS1.1.1681049796.186.1.1681053701.60.0.0; _clck=1bkkm1u|1|fan|0; dau_lp=%2Fpublic%2Fjobs%2Fsearch%3Fcategory_id%3D226%26keep_search_criteria%3Dtrue%26order%3Dnew%26hide_expired%3Dtrue; dau_visit_user_id=5331054; __lt__sid=b1a8b11c-c815de04; main_menu_role=employee; _im_ses.1008949=1; _rt.xd=3cccdcea; _clsk=1t3wo33|1681134195715|89|1|u.clarity.ms/collect; keen_session={%22uuid%22:%2201325914-a396-4bf0-96f5-0b8de596585f%22%2C%22timestamp%22:1681134198}; _ga_WC7RFDVS0V=GS1.1.1681122121.192.1.1681134198.32.0.0"
}

resp = requests.get("https://crowdworks.jp/attachments/44170997.gz?download=true", headers = headers)

import codecs
# resp.content
f = codecs.open("a.tz", "wb")
f.write(resp.content)
f.close()