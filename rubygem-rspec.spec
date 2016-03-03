%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global	gem_name	rspec

Summary:	Behaviour driven development (BDD) framework for Ruby
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	3.4.0
Release:	4%{?dist}
Group:		Development/Languages
License:	MIT
URL:		http://rspec.info
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}rubygems
# rspec dependencies have different versions
Requires: %{?scl_prefix}rubygem(rspec-core) => 3.4.0
Requires: %{?scl_prefix}rubygem(rspec-core) < 3.5
Requires: %{?scl_prefix}rubygem(rspec-expectations) => 3.4.0
Requires: %{?scl_prefix}rubygem(rspec-expectations) < 3.5
Requires: %{?scl_prefix}rubygem(rspec-mocks) => 3.4.0
Requires: %{?scl_prefix}rubygem(rspec-mocks) < 3.5
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires:	%{?scl_prefix_ruby}rubygems-devel
BuildRequires:	%{?scl_prefix_ruby}ruby(release)
BuildArch:	noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
RSpec is a behaviour driven development (BDD) framework for Ruby.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem specification %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%files
%dir	%{gem_instdir}
%{gem_instdir}/lib
%license	%{gem_instdir}/LICENSE.md
%doc	%{gem_instdir}/README.md
%exclude %{gem_cache}
%{gem_spec}

%files	doc
%doc	%{gem_docdir}

%changelog
* Tue Feb 23 2016 Pavel Valena <pvalena@redhat.com> - 3.4.0-4
- Fix rubygem-rspec-* version Requires

* Mon Feb 22 2016 Pavel Valena <pvalena@redhat.com> - 3.4.0-3
- Update to 3.4.0

* Fri Jan 16 2015 Josef Stribny <jstribny@redhat.com> - 2.14.1-1
- Update to 2.14.1

* Mon May 20 2013 Josef Stribny <jstribny@redhat.com> - 2.11.0-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Wed Feb 27 2013 Vít Ondruch <vondruch@redhat.com> - 2.11.0-2
- Rebuild to fix documentation vulnerability due to CVE-2013-0256.

* Tue Jul 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.11.0-1
- Update to Rspec 2.11.0.
- Specfile cleanup.

* Fri Mar 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.8.0-2
- Rebuilt for scl.

* Mon Mar 05 2012 Vít Ondruch <bkabrda@redhat.com> - 2.8.0-1
- Update to RSpec 2.8.0.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.1-1
- Update from Marek Goldmann <mgoldman@redhat.com>
  - Updated to 1.3.1
  - Patch to make it work with Rake >= 0.9.0.beta.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Michael Stahnke <stahnma@fedpraproject.org> - 1.3.0-2
- Removed 404 URL in the description (bug 515042)

* Fri Apr 09 2010 Michael Stahnke <stahnma@fedpraproject.org> - 1.3.0-1
- Updated to 1.3.0

* Wed Dec 09 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.9-1
- New Version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.7-1
- New Version

* Fri Mar 27 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.2-1
- New Version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 08 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.11-1
- New Version

* Mon Nov 03 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-3
- Updating to require ruby(abi)

* Mon Oct 13 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-1
- New version

* Wed May 14 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.3-1
- Initial package
