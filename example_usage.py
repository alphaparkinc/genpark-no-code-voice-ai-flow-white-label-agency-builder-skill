from client import NoCodeVoiceAiFlowWhiteLabelAgencyBuilderClient

def main():
    client = NoCodeVoiceAiFlowWhiteLabelAgencyBuilderClient()
    res = client.build_flow("dental", {"name": "SmilePro Agency"})
    print(f"Industry: {res['generated_flow']['industry']}")
    print(f"Deployment Time: {res['estimated_deployment_minutes']} minutes")
    pkg = res["white_label_package"]
    print(f"White-Label: {pkg['brand_name']} @ {pkg['custom_domain']} (markup: {pkg['reseller_markup_pct']}%)")
    print("Flow Nodes:")
    for node in res["generated_flow"]["nodes"]:
        print(f"  Node {node['id']}: {node['name']}")

if __name__ == "__main__":
    main()
