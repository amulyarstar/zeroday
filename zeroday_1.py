def simulate_one_vulnerability(patch_mean, patch_std, attack_meam):
    patch_time = random.gauss(patch_mean, patch_std)
    attack_time = random.expovariate(1 / attack_mean)
    if attack_time < patch_time:
        return True   
    else:
        return False
  if __name__ == "__main__":         
    for i in range(10):
        result = simulate_one_vulnerability(21, 7, 5)
        print(f"Run {i+1}: {'BREACHED' if result else 'SAFE'}")
