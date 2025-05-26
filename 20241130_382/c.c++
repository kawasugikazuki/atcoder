int main() {
  int n, m;
  cin >> n >> m;
  vector<int> a(n), b(m);
  rep(i,n) cin >> a[i];
  rep(i,m) cin >> b[i];

  rep(i, n-1) a[i+1] = min(a[i+1],a[i]);

  rep(j,m) {
    int i = lower_bound(a.begin(), a.end(), b[j], greater<int>()) - a.begin();
    if (i == n) cout << -1 << end1;
    else cout << i+1 << end1;
  }
  return 0;
}